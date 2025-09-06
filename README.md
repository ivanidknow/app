# app — FastAPI сервис с /ping

Мини-сервис на FastAPI (Uvicorn), эндпоинт `/ping`. Собирается Docker’ом, публикуется в GitLab Registry, деплоится в Kubernetes чартом из репозитория `infra`.

## Быстрый старт локально

```bash
# 1) Запуск без Docker
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000

# 2) Проверка
curl -s http://127.0.0.1:8000/ping   # -> pong