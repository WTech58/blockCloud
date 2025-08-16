FROM ubuntu:latest

RUN apt-get update && apt-get install git -y

RUN git clone https://github.com/WTech58/blockCloud.git 
RUN cd blockCloud/src/install && \
    chmod +x ./blockcloud && \
    ./blockcloud init
RUN python src/start.py
