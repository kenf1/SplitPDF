FROM python:3.11.3-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

COPY ./setup ./setup
RUN pip3 install -r ./setup/requirements.txt
COPY ./app ./app

EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["python3","-m","streamlit","run","./app/Home.py","--server.port=8501","--server.address=0.0.0.0"]