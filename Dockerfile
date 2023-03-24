FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python", "main.py"]
