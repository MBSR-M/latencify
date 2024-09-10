# Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY rate_limiting_service rate_limiting_service

CMD ["python", "rate_limiting_service/main.py"]
