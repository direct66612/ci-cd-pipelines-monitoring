# CI/CD Pipeline for Python App with Docker and Jenkins

## Проект

Цей репозиторій містить простий Python-додаток, який запускає HTTP-сервер. Для автоматизації побудови, тестування та розгортання додатку налаштовано Jenkins пайплайн.

## Опис проекту

1. **app.py** — простий Python-сервер, який відповідає на HTTP-запити.
2. **Dockerfile** — контейнеризація Python-додатку.
3. **Jenkinsfile** — конфігурація CI/CD пайплайна для Jenkins, що включає етапи:
   - Збірка Docker-образу.
   - Розгортання Docker-контейнера.
   - Тестування за допомогою HTTP-запиту.
   - Зупинка контейнера та видалення образу.

## Налаштування

### 1. Створіть репозиторій на GitHub

- Створіть репозиторій на GitHub і завантажте код.
- Замініть `REPO_URL` у `Jenkinsfile` на URL вашого репозиторія.

### 2. Налаштування Docker

- Встановіть Docker на вашу машину або сервер.
- Для запуску контейнера використовується Dockerfile, який будує образ і запускає сервер.

### 3. Налаштування Jenkins

1. Встановіть Jenkins і налаштуйте плагіни для роботи з Docker.
2. Створіть новий проект у Jenkins:
   - Тип проекту: Pipeline.
   - Вкажіть URL репозиторія та вкажіть шлях до `Jenkinsfile`.
3. В Jenkins, натисніть кнопку "Build Now" для запуску пайплайну. Якщо все налаштовано правильно, Jenkins виконає етапи збірки образу, тестування та розгортання.

### 4.Перевірка

1.На сторінці пайплайну можна побачити, як кожен етап успішно виконується або отримує повідомлення про помилку.
2.Також можно побачити що сервер відвопідає статусом 200.
![Скріншот успішного білду](images/succes-build.png)
![Скріншот робочого серверу](images/succes-server.png)
