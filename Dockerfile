FROM python:3.7-alpine

RUN apk add --no-cache g++ make

COPY requirements/* /tmp/

RUN pip install -r /tmp/prod.txt

RUN rm /tmp/*.txt

WORKDIR /opt
