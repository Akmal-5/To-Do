# 📝 **To-Do**  
**Backend API для умного управления задачами с JWT-авторизацией**


[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python)](https://www.python.org)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-Async-FF4B4B?style=for-the-badge)](https://www.sqlalchemy.org)
[![JWT](https://img.shields.io/badge/JWT-Auth-black?style=for-the-badge)](https://jwt.io)

> Современный асинхронный REST API для управления личными задачами.  
> Полная авторизация + CRUD задач с фильтрацией.  
> Сделано на FastAPI + SQLAlchemy (async) 🚀

---

## ✨ **Возможности проекта**

- ✅ **Регистрация и авторизация** пользователей (JWT-токен)
- ✅ **Полностью защищённые** эндпоинты задач (только свои задачи)
- ✅ **CRUD** операций над задачами:
  - Создание новой задачи
  - Получение списка задач (с фильтром по названию)
  - Обновление задачи
  - Удаление задачи
- ✅ **Автоматическое создание** таблиц БД при запуске
- ✅ **Асинхронная** работа с базой данных
- ✅ Чёткое разделение по тегам в Swagger-документации

---

## 🛠 **Технологический стек**

| Технология          | Назначение                          |
|---------------------|-------------------------------------|
| **FastAPI**         | Основной фреймворк API             |
| **SQLAlchemy**      | Асинхронный ORM                     |
| **Pydantic**        | Валидация моделей (User, UserTasks, UserLog) |
| **JWT**             | Авторизация (encode/decode)         |
| **AsyncSession**    | Асинхронная работа с БД             |
| **Python 3.11+**    | Язык разработки                     |
