FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

USER root

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app; exit 0
WORKDIR /app
COPY ./app /app

RUN adduser -D user; exit 0
USER user
