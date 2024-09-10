# Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY cache_management_service cache_management_service

# Copy the logging configuration if necessary
 COPY logging_service/log_config.py logging_service/log_config.py/

CMD ["python", "cache_management_service/main.py"]
