FROM ubuntu:22.04
# FROM python:3.10-slim

ENV TZ=Europe/Berlin

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    unoconv \
    libreoffice \
    python3-pip && \
    pip3 install --upgrade pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt
COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

VOLUME /app/volums_fitxes_tecniques

CMD ["python3", "fitxes_tecniques.py"]