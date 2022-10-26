FROM python:3.10

WORKDIR /

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240

RUN pip freeze > requirements.txt .

COPY . .
COPY ./requirements.txt /requirements.txt
COPY openapi.yaml /swagger.yaml

ENV PYTHONPATH /
ENV SWAGGER_JSON "/swagger.yaml"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt



