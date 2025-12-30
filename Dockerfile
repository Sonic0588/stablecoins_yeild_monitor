FROM python:3.11-slim

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "-m", "src.main"]

