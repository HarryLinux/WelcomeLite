# Python image build
FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

# Docker image system dependencies to connect to Postgres
RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    postgresql \
    libpq-dev


COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY manage.py ./manage.py
COPY WelcomeLite ./WelcomeLite
COPY WelcomeLiteApp ./WelcomeLiteApp

EXPOSE 8000
