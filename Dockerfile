# Используем за основу контейнера Ubuntu 20.04 LTS
FROM python:3.8.10

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/

# Добавляем необходимые репозитарии и устанавливаем пакеты
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get install -y supervisor

COPY . /code/