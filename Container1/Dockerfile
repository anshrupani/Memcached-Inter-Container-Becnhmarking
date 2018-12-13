FROM ubuntu:16.04
      
MAINTAINER Ansh Rupani <ansh.rupani@mailbox.tu-dresden.de>

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y openssh-server libevent-dev gcc g++ make
RUN wget http://www.memcached.org/files/memcached-1.4.33.tar.gz && tar -zxvf memcached-1.4.33.tar.gz 
RUN cd memcached-1.4.33 && ./configure && make && make install

RUN useradd -u 1000 ubuntu && mkdir /var/run/sshd && mkdir -p /home/ubuntu/.ssh && chown -R ubuntu /home/ubuntu
COPY authorized_keys home/ubuntu/.ssh

EXPOSE 22 11211
CMD ["/usr/sbin/sshd", "-D"]
