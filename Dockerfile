FROM ubuntu:latest

RUN apt update&&apt install -y python3 python3-pip

RUN python3 -m pip install flask docker

COPY src/app /app

WORKDIR /app

RUN python3 router.py
