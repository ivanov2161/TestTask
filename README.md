## Тестовое задание
В проекте использовал **Django REST Framework** и **Celery**

Выполнена основная задача, без дополнительных заданий 

*Ссылка на задание: https://www.craft.do/s/n6OVYFVUpq0o6L*

## Описание
Celery каждые 30 секунд проверяет базу данных рассылок, и если есть подходящие рассылки - запускается функция отправки сообщений клиентам

## Требуется установить

Установка библиотек
```bash
pip install -r requirements.txt
```
1. Установить Redis согласно инструкции

https://redis.io/docs/getting-started/installation/

2. Создать и применить миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Добавить в переменные окружения значения URL и TOKEN
## Запуск

1. Запустить Redis
```bash
sudo service redis-server start
```
2. Запустить сервер
```bash
python manage.py runserver
```
3. Запустить Celery
```bash
celery -A InterviewTask worker -l info
```
4. Запустить Beat
```bash
celery -A InterviewTask beat -l info
```

## Список API

* http://127.0.0.1:8000/api/mailing/ - Рассылки
* http://127.0.0.1:8000/api/client/ - Клиенты
* http://127.0.0.1:8000/api/message/ - Сообщения
* http://127.0.0.1:8000/api/mailing/fullstats - Полная статистика
* http://127.0.0.1:8000/api/mailing/<id>/stats - Статистика по конкретной рассылке
