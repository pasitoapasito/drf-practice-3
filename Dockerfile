FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /usr/src/app