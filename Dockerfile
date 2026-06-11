FROM dockerhub.timeweb.cloud/library/python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Установка uv без использования внешних контейнеров ghcr.io
RUN pip install --no-cache-dir uv

COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

COPY . .

# Запуск с правильным путем к вашей папке app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
