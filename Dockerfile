FROM python:3.12-slim
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "health_check.py"]
RUN apt-get update && apt-get install -y docker.io

