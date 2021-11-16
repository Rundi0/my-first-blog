Запуск в docker:
    docker-compose up


Для нативного запуска:
    Создания вируального среды:
        pipenv shell
    
    Установка зависимостей:
        pipenv install
     
    Мигрировать схемы базы данных:
        python manage.py migrate
     
    Создания локального суперпользователя:
        python manage.py createsuperuser
     
    Запуск сервера локального веб сервера:
        python manage.py runserver
    
    Запуск celery:
        celery -A mysite worker -l INFO
        sudo celery multi start 1
    
    Запуск демона docker wsl:
        sudo /etc/init.d/docker start
    
        sudo docker run -d -p 5672:5672 rabbitmq &&
        sudo docker run -d -p 6379:6379 redis
