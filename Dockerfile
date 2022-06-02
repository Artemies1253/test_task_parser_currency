FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/tt_bs

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/tt_bs
