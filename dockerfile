FROM python:3.8-buster

ENV PYTHONBUFFERED=1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn yiwuexpert.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000
