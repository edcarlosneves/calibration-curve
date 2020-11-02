FROM python:3

COPY requirements.txt /

RUN pip3 install -r /requirements.txt

COPY . /usr/src/app

WORKDIR /usr/src/app