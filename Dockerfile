FROM python:3.12-slim

WORKDIR /app
ENV PYTHONPATH=/app

COPY minizip/ minizip/

ENTRYPOINT ["python", "-m", "minizip.cli"]
