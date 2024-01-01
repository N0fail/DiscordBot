FROM python:3.11-alpine
LABEL authors="n0fail"

RUN apk update && \
    apk add --no-cache ffmpeg opus opus-dev

ENV LIBOPUS_PATH="/usr/lib/libopus.so"

COPY requirements.txt /opt
RUN pip install -r /opt/requirements.txt

WORKDIR /opt/src
ENTRYPOINT python bot.py