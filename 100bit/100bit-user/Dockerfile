FROM ubuntu:22.04

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install pycryptodome
RUN apt install xinetd -y

COPY ./Cipher.py /root/Cipher.py
COPY ./100bit.py /root/100bit.py
COPY ./flag /flag
COPY ./100bit /etc/xinetd.d/100bit

RUN echo "100bit	10002/tcp" >> /etc/services

CMD ["/usr/sbin/xinetd","-dontfork"]