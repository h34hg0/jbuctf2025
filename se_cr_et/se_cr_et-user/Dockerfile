FROM ubuntu:22.04

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install pycryptodome
RUN apt install xinetd -y

COPY ./Cipher.py /root/Cipher.py
COPY ./se_cr_et.py /root/se_cr_et.py
COPY ./flag /flag
COPY ./se_cr_et /etc/xinetd.d/se_cr_et

RUN echo "se_cr_et	10001/tcp" >> /etc/services

CMD ["/usr/sbin/xinetd","-dontfork"]