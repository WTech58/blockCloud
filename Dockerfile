FROM ubuntu:latest

RUN apt update&&apt install python3

RUN pip install flask docker

COPY src/app /app

WORKDIR /app

RUN python router.py
