FROM ubuntu:16.04

MAINTAINER Pereskokov Vladislav

RUN apt-get update
RUN apt-get install -y build-essential wget curl python2.7

RUN mkdir -p /root/ok.ru
ADD . /root/ok.ru

RUN ./root/ok.ru/scripts/grid.sh
RUN ./root/ok.ru/scripts/node_linux_64.sh

CMD python2.7 run_tests.py

