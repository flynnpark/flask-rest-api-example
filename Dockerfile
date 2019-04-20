FROM python:3.7-slim

ENV NAME TEST

LABEL Name=flask-rest-api-example Version=0.0.1
EXPOSE 5000

WORKDIR /app
ADD . /app

# Using pip:
RUN pip install -r requirements.txt
CMD ["python", "api.py"]