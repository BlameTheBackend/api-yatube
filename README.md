## Описание
Краткое API для блога: пользователи, посты, группы, комментарии. Реализовано на Django REST Framework. Предназначено для обучения и тестирования запросов к REST API.

## Быстрый старт (локально)
1. Клонировать репозиторий и перейти в папку проекта:
    - git clone https://github.com/ThinkLikeHorsie/api-yatube
    - cd yatube_api
2. Создать и активировать виртуальное окружение:
    - python -m venv venv
    - source venv/bin/activate  (Windows: venv\Scripts\activate)
3. Установить зависимости:
    - pip install -r requirements.txt
4. Выполнить миграции:
    - python manage.py migrate
5. Запустить сервер:
    - python manage.py runserver

## Примеры запросов и ответов

*POST .../api/v1/posts/*

```json
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
} 
```

Пример ответа:
```json
{
    "id": 14,
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
} 
```

---

*POST .../api/v1/posts/14/comments/*

```json
{
    "text": "тест тест",
}
```

Пример ответа:
```json
{
    "id": 4,
    "author": "anton",
    "post": 14,
    "text": "тест тест",
    "created": "2021-06-01T10:14:51.388932Z"
} 
```
---

*GET .../api/v1/groups/2/*

Пример ответа:
```json
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
} 
```

## Тесты
- Запустить тесты в Postman:
  - cd postman_collection
  - bash set_up_data.sh
  - Импортировать файл CRUD_for_yatube.postman_collection.json в Postman
  - Запустить тесты
- Линтинг:
  - flake8
