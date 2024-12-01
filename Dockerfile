FROM ubuntu:latest

RUN apt update&&apt install python3.9 python3-pip

RUN pip3 install flask docker

COPY src/app /app

WORKDIR /app

RUN python router.py
