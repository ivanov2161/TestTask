## Тестовое задание
В проекте использовал **Django REST Framework** и **Celery**

* Python version - 3.10.4
* Django version - 4.1
* djangorestframework version - 3.13.1
* Celery version - 5.2.7


*Ссылка на задание: https://www.craft.do/s/n6OVYFVUpq0o6L*

[//]: # (**На данный момент выполнено:**)

[//]: # ()
[//]: # (* добавления нового клиента в справочник со всеми его атрибутами)

[//]: # (* обновления данных атрибутов клиента)

[//]: # (* удаления клиента из справочника)

[//]: # (* добавления новой рассылки со всеми её атрибутами)

[//]: # (* получения общей статистики по созданным рассылкам и количеству отправленных сообщений по ним с группировкой по статусам)

[//]: # (* получения детальной статистики отправленных сообщений по конкретной рассылке)

[//]: # (* обновления атрибутов рассылки)

[//]: # (* удаления рассылки)

[//]: # (* обработки активных рассылок и отправки сообщений клиентам)


## Требуется установить

Установка библиотек
```bash
pip install -r requirements.txt
```
Установить Redis согласно инструкции

https://redis.io/docs/getting-started/installation/install-redis-on-windows/

Создать и применить миграции в базу данных:
```bash
python manage.py makemigrations
python manage.py migrate
```
## Запуск

Запустить Redis через оболочку Ubuntu
```bash
sudo service redis-server start
```
Запустить сервер
```bash
python manage.py runserver
```
Запустить Celery
```bash
celery -A InterviewTask worker -l info
```
Запустить Beat
```bash
celery -A InterviewTask beat -l info
```
