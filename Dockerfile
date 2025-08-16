FROM ubuntu:latest

RUN apt-get install git -y

RUN git clone https://github.com/WTech58/blockCloud.git 
RUN cd blockCloud/src/install
RUN chmod +x ./blockcloud
RUN ./blockcloud init
RUN cd ..
RUN python start.py
