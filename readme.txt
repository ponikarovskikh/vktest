Краткая документация:

Запуск сервиса:
Для запуска сервиса необходимо склонировать репозиторий и установить зависимости. После этого можно запустить сервер командой:


python manage.py runserver
Сервер запустится на адресе http://localhost:8000/

API сервиса:
Сервис предоставляет следующие REST API:

POST /api/register/: регистрация нового пользователя

Запрос:

json

{
    "username": "user1"
}
Ответ:


{
    "id": 1,
    "username": "user1"
}
POST /api/friend-request/: отправка заявки в друзья

Запрос:


{
    "from_user": 1,
    "to_user": 2
}
Ответ:


{
    "id": 1,
    "from_user": 1,
    "to_user": 2,
    "status": "PENDING"
}
POST /api/friend-request/{id}/accept/: принятие заявки в друзья

Ответ:


{
    "id": 1,
    "from_user": 1,
    "to_user": 2,
    "status": "ACCEPTED"
}
POST /api/friend-request/{id}/reject/: отклонение заявки в друзья

Ответ:


{
    "id": 1,
    "from_user": 1,
    "to_user": 2,
    "status": "REJECTED"
}
GET /api/friend-requests/sent/: получение списка исходящих заявок в друзья

Ответ:


[    {        "id": 1,        "from_user": 1,        "to_user": 2,        "status": "PENDING"    }]
GET /api/friend-requests/received/: получение списка входящих заявок в друзья

Ответ:


[    {        "id": 1,        "from_user": 1,        "to_user": 2,        "status": "PENDING"    }]
GET /api/friends/: получение списка друзей пользователя

Ответ:


[    {        "id": 2,        "username": "user2"    }]
GET /api/friend-status/: получение статуса дружбы с другим пользователем

Запрос:


{
    "user1": 1,
    "user2": 2
}
Ответ:



{
    "status": "FRIENDS"
}
POST /api/unfriend/: удаление друга из списка друзей

Запрос:


{
    "user1": 1,
    "user2": 2
}
