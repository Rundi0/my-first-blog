Для запуска проекта нужно выполнить следующие действия:
Установка инструмента virtualenv(если еще не установлен):
    pip install virtualenv
 
Создание новой виртуальной среды(вместо [name] можно вписывать любоє имя например 'virtualspace'):
    virtualenv [name]
 
Активация виртуальной среды
    source [name]/bin/activate         #linux
    [name]\Scripts\activate.bat        #windows cmd
 
Восстановление зависимостей:
    pip install -r requirements.txt
 
Мигрировать схемы базы данных:
    python manage.py migrate
 
Создания локального суперпользователя:
    python manage.py createsuperuser
 
Запуск сервера локального веб сервера:
    python manage.py runserver
