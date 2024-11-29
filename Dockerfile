FROM ubuntu:latest

RUN apt update&&apt install python3.9

RUN pip install flask docker

RUN cd src/app&&python router.py
