# Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY cache_management_service cache_management_service

CMD ["python", "cache_management_service/main.py"]
