FROM python:3.11-slim
WORKDIR /app
COPY app/worker.py .
CMD ["python", "worker.py"]
