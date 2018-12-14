FROM ubuntu:16.04
      
MAINTAINER Ansh Rupani <ansh.rupani@mailbox.tu-dresden.de>

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y openssh-server libevent-dev gcc g++ make
RUN wget https://github.com/twitter/twemperf/archive/v0.1.1.tar.gz && tar -xvf v0.1.1.tar.gz
RUN apt-get install -y autoconf
RUN cd twemperf-0.1.1 && autoreconf -fvi && ./configure && make && make install 
RUN apt-get install -y python python-setuptools && wget https://bitbucket.org/db7/dude/get/v3.1.tar.gz && tar -xf v3.1.tar.gz && cd db7-dude-e0a2a25bd2a7 && python setup.py install
RUN apt-get install -y r-base

RUN useradd ubuntu
RUN mkdir /var/run/sshd && mkdir -p /home/ubuntu/.ssh

COPY run.sh run.sh
COPY Dudefile Dudefile
COPY graphs.R graphs.R
COPY Benchmark.py Benchmark.py

RUN chown -R ubuntu /home/ubuntu

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
