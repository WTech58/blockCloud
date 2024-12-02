FROM ubuntu:latest

RUN apt update&&apt install -y software-properties-common

RUN apt install -y python3.9

RUN python3 -m pip --version

RUN python3 -m pip install flask docker

COPY src/app /app

WORKDIR /app

RUN python3 router.py
