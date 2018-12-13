FROM ubuntu:16.04
      
MAINTAINER Ansh Rupani <ansh.rupani@mailbox.tu-dresden.de>

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y openssh-server libevent-dev gcc g++ make
RUN wget http://www.memcached.org/files/memcached-1.4.33.tar.gz && tar -zxvf memcached-1.4.33.tar.gz 
RUN cd memcached-1.4.33 && ./configure && make && make install

EXPOSE 22 11211
CMD ["/usr/sbin/sshd", "-D"]
