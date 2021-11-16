# Используем за основу контейнера Ubuntu 20.04 LTS
FROM python:3.8-slim

# Добавляем необходимые репозитарии и устанавливаем пакеты
RUN apt-get update
#RUN apt-get install -y python3-pip
RUN apt-get install -y supervisor
RUN pip3 install pipenv

RUN mkdir /code
WORKDIR /code
COPY Pipfile* /code/
COPY Pipfile.lock /code/

RUN pipenv install --deploy --system

COPY . /code/

RUN python manage.py migrate 