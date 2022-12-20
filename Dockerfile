# FROM python:3-alpine3.7
FROM python:3.8-slim-buster
RUN mkdir /app
RUN mkdir /app/webApp
RUN mkdir /app/models

WORKDIR /app

ADD ./webApp /app/webApp
ADD ./models /app/models
ADD application.py /app
ADD requirements.txt /app
ADD params.yaml /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# EXPOSE 3000

CMD python application.py







