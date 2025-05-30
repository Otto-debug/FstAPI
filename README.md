# 🧠 FastAPI + Telegram Bot Project

## 📦 Стек
- **Backend**: FastAPI + SQLAlchemy + PostgreSQL
- **Bot**: Python Telegram Bot
- **DB**: PostgreSQL (в контейнере)
- **Docker**: Используется `docker-compose` для поднятия всех сервисов

## 📁 Структура проекта

```
FstAPI/
│
├── backend/
│   ├── app/                 # Код FastAPI-приложения
│   │   ├── main.py          # Точка входа
│   │   ├── models.py        # SQLAlchemy модели
│   │   ├── schemas.py       # Pydantic схемы
│   │   ├── database.py      # Подключение к БД
│   │   ├── auth.py          # JWT авторизация
│   │   ├── utils.py         # Хелперы (например, хэширование)
│   ├── requirements.txt
│   └── Dockerfile
│
├── bot/
│   ├── bot.py               # Telegram-бот
│   ├── config.py
│   ├── database.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── .env                     # Переменные окружения
├── docker-compose.yml
└── README.md
```

## ⚙️ Переменные окружения (`.env`)

Создай файл `.env` в корне проекта и добавь:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=fastapi_db

SECRET_KEY=supersecretkey
BOT_TOKEN=your_telegram_bot_token
```

## 🐳 Запуск проекта

1. Собери и запусти контейнеры:

```bash
docker-compose up --build
```

2. Проверь, что API доступно по адресу:  
   👉 http://localhost:8000

## 📌 Доступные endpoints

### POST `/register`
Регистрация пользователя.

**Пример запроса:**
```json
{
  "username": "johndoe",
  "name": "John",
  "password": "secret"
}
```

### POST `/login`
Аутентификация и получение токена.

**Пример запроса:**
```json
{
  "username": "johndoe",
  "password": "secret"
}
```

**Ответ:**
```json
{
  "access_token": "your.jwt.token",
  "token_type": "bearer"
}
```

### POST `/connect-telegram`
Связать Telegram ID с пользователем (нужен токен в заголовке).

**Заголовок:**  
`Authorization: Bearer <access_token>`

**Пример запроса:**
```json
{
  "telegram_id": 123456789
}
```

## 🤖 Telegram Bot

Бот находится в папке `bot/`. Он подключается к той же базе данных и может использовать telegram_id для связи с пользователем.

## 🧪 Полезные команды

### Остановить и удалить контейнеры:
```bash
docker-compose down
```

### Перезапуск с пересборкой:
```bash
docker-compose up --build
```

## ✅ TODO
- [ ] Добавить миграции Alembic
- [ ] Docker Healthchecks
- [ ] Тесты (pytest)
- [ ] Обработка ошибок в боте
