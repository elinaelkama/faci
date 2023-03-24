FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENV DISCORD_TOKEN=${DISCORD_TOKEN}
CMD ["python", "main.py"]
