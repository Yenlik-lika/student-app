# student-app

Учебное Flask-приложение «Student Information System» для СӨЖ №1 (вариант 22):
настройка публикации Docker-образа в container registry (GitHub Container Registry, ghcr.io) через GitHub Actions.

## Конвейер (.github/workflows/ci.yml)

1. **test** — установка зависимостей и запуск `pytest`.
2. **build-and-push** — после успешных тестов (только при push в `main`): вход в ghcr.io, сборка Docker-образа и публикация с тегами `latest` и `sha-<commit>`.

## Запуск образа

```bash
docker pull ghcr.io/yenlik-lika/student-app:latest
docker run -p 5000:5000 ghcr.io/yenlik-lika/student-app:latest
```

Эндпоинты: `/`, `/courses`, `/health`.
