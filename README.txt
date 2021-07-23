Для запуска проекта нужно виполнить следуйщие действия:
Установка инструмента virtualenv(если еще не установлен):
    pip install virtualenv

Создание новой виртуальной среды:
    virtualenv [name]

Активация виртуальной среды
    source [name]/bin/activate         #linux
    [name]\Scripts\activate.bat        #windows

Восстановление зависимостей:
    pip install -r requirements.txt

Мигрировать схеми базы даних:
    python manage.py migrate

Создания локального суперпользователя:
    python manage.py createsuperuser