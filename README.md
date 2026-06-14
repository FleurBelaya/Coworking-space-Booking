# Сайт бронирования коворкинг пространств 

Команды для начала работы:
Склонировать репозиторий
Перейти в терминал
cp .env.example .env
(Надо будет поменять переменные окружения в .env)
docker compose up -d --build
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py seed_db
(загрузка тестовых данных: брони, пространства и тд)
docker compose exec backend python manage.py createsuperuser
docker compose exec backend pytest

# 📌 API Endpoints

Сервис предоставляет REST API для управления пространствами и бронированиями.

Базовый URL (локально):
http://127.0.0.1:8000/

---

## 🏢 Пространства (Spaces)

### Получить список всех пространств
GET /spaces/

---

### Создать пространство
POST /spaces/create/

---

### Удалить пространство
DELETE /spaces/{id}/delete/

где `{id}` — идентификатор пространства

---

## 👤 Пространства владельца

### Получить пространства конкретного владельца
GET /owners/{owner_id}/spaces/

где `{owner_id}` — ID владельца

---

## 📅 Бронирования (Reservations)

### Создать бронирование
POST /reservations/create/

---

### Удалить бронирование
DELETE /reservations/{id}/delete/

где `{id}` — идентификатор бронирования

---

## 📌 Примеры запросов

### ➕ Создание пространства

```http
POST /spaces/create/
Content-Type: application/json

{
  "name": "Open Space",
  "price": 1000,
  "owner": 1
}

