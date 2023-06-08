FROM python:3.11.3-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

COPY ./setup ./setup
COPY ./app ./app
RUN pip3 install -r ./setup/requirements.txt