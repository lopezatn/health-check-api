FROM python:3.12-slim
COPY . .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y docker.io
CMD ["python3", "health_check.py"]
