#!/usr/bin/bash
set -euo pipefail

FORCE=false
for arg in "$@"; do
  case "$arg" in
    -f|--force)
      FORCE=true
      ;;
  esac
done

# Load .env (requires DEPLOY_SERVER and DEPLOY_USER)
if [[ ! -f .env ]]; then
  echo "Error: .env file not found" >&2
  exit 1
fi
set -a
source <(sed 's/\r$//' .env)
set +a

if [[ -z "${DEPLOY_SERVER:-}" || -z "${DEPLOY_USER:-}" ]]; then
  echo "Error: DEPLOY_SERVER and DEPLOY_USER must be set in .env" >&2
  exit 1
fi

# Make sure all changes are committed to git
if [[ "$FORCE" != "true" ]]; then
  if [[ -n "$(git status --porcelain 2>/dev/null)" ]]; then
    echo "Error: Uncommitted changes detected. Please commit before deploying or use --force." >&2
    exit 1
  fi
fi

IMAGE_NAME="faci-bot"
IMAGE_REF="$(grep -m1 -E '^[[:space:]]*image:' docker-compose.yml | sed -E 's/^[[:space:]]*image:[[:space:]]*//' | tr -d '\r')"
IMAGE_TAG="${IMAGE_REF##*:}"
TAR_FILE="${IMAGE_NAME}.tar"
REMOTE_DIR="/app/faci-bot"
BUILD_CTX_DIR="$(mktemp -d /tmp/faci-build-XXXXXX)"

cleanup() {
  rm -rf "${BUILD_CTX_DIR}" 2>/dev/null || true
}
trap cleanup EXIT

echo "Preparing clean build context in ${BUILD_CTX_DIR}..."
if command -v rsync >/dev/null 2>&1; then
  rsync -a --delete \
    --exclude='.git/' \
    --exclude='.venv/' \
    --exclude='venv/' \
    --exclude='__pycache__/' \
    --exclude='.pytest_cache/' \
    --exclude='.mypy_cache/' \
    --exclude='.ruff_cache/' \
    --exclude='.env' \
    ./ "${BUILD_CTX_DIR}/"
else
  tar -cf - \
    --exclude='.git' \
    --exclude='.venv' \
    --exclude='venv' \
    --exclude='__pycache__' \
    --exclude='.pytest_cache' \
    --exclude='.mypy_cache' \
    --exclude='.ruff_cache' \
    --exclude='.env' \
    . | tar -xf - -C "${BUILD_CTX_DIR}"
fi${DEPLOY_USER}@${DEPLOY_SERVER}:${REMOTE_DIR}/${TAR_FILE}"

echo "Loading image and restarting on server..."
ssh "${DEPLOY_USER}@${DEPLOY_SERVER}" bash <<EOF
  set -euo pipefail
  cd ${REMOTE_DIR}
  docker load -i ${TAR_FILE}
  sed -i -E "0,/^[[:space:]]*image:/s#^([[:space:]]*image:[[:space:]]*).*$#\1${IMAGE_REF}#" docker-compose.yml
  docker compose down
  docker compose up -d
  rm -f ${TAR_FILE}
EOF

echo "Cleaning up local tar file..."
rm -f "${TAR_FILE}"

echo "Deployment complete."