FROM ubuntu:latest

RUN apt update&&apt install python3

RUN python3 -m pip install flask docker

COPY src/app /app

WORKDIR /app

RUN python3 router.py
