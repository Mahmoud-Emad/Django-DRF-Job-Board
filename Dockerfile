FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add libffi-dev openssl-dev cargo
    
COPY requirements.txt /code/
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /code/

RUN adduser -D user
USER user