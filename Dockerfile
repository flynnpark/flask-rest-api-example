FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV NAME TEST

LABEL Name=flask-rest-api-example Version=0.0.2

COPY ./app /app

RUN pip install -r requirements.txt