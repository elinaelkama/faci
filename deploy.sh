#!/usr/bin/bash
set -euo pipefail

# Load .env (requires DEPLOY_SERVER and DEPLOY_USER)
if [[ ! -f .env ]]; then
  echo "Error: .env file not found" >&2
  exit 1
fi
source .env

if [[ -z "${DEPLOY_SERVER:-}" || -z "${DEPLOY_USER:-}" ]]; then
  echo "Error: DEPLOY_SERVER and DEPLOY_USER must be set in .env" >&2
  exit 1
fi

# Make sure all changes are committed to git
if [[ -n "$(git status --porcelain)" ]]; then
  echo "Error: Uncommitted changes detected. Please commit before deploying." >&2
  exit 1
fi

IMAGE_NAME="faci-bot"
IMAGE_TAG="$(grep 'image:' docker-compose.yml | head -1 | awk -F':' '{print $NF}' | tr -d ' ')"
TAR_FILE="${IMAGE_NAME}.tar"
REMOTE_DIR="/app/faci-bot"

echo "Building Docker image ${IMAGE_NAME}:${IMAGE_TAG}..."
docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" .

echo "Saving image to ${TAR_FILE}..."
docker save "${IMAGE_NAME}:${IMAGE_TAG}" -o "${TAR_FILE}"

echo "Copying image to ${DEPLOY_USER}@${DEPLOY_SERVER}:${REMOTE_DIR}/${TAR_FILE}..."
scp "${TAR_FILE}" "${DEPLOY_USER}@${DEPLOY_SERVER}:${REMOTE_DIR}/${TAR_FILE}"

echo "Loading image and restarting on server..."
ssh "${DEPLOY_USER}@${DEPLOY_SERVER}" bash <<EOF
  set -euo pipefail
  cd ${REMOTE_DIR}
  docker load -i ${TAR_FILE}
  docker compose down
  docker compose up -d
  rm -f ${TAR_FILE}
EOF

echo "Cleaning up local tar file..."
rm -f "${TAR_FILE}"

echo "Deployment complete."