FROM python:3.10-alpine

COPY . /app
WORKDIR /app
RUN apk add gcc
RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base

RUN apk add netcat-openbsd

RUN pip install -r requirements.txt

RUN mkdir -p home/app/web/static
RUN mkdir -p home/app/web/media

RUN chmod 777 home/app/web/static
RUN chmod 777 home/app/web/media