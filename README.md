# URL Shortener API

A simple REST API service for shortening long URLs.

This project was created as a Junior Python Backend project. It implements basic CRUD operations for shortened URLs, redirects users to the original URL, and tracks the number of clicks.

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Docker
* Docker Compose
* Hashids

## Features

* Create a short URL from a long URL
* Get information about a short URL
* Redirect from a short URL to the original URL
* Track click statistics
* Update the original URL
* Delete a short URL
* Get a list of all shortened URLs
* Run the project with Docker Compose

## Project Structure

```text
.
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── crud.py
│   │       ├── generator_url.py
│   │       ├── models.py
│   │       └── url_shortener_api.py
│   ├── schemas/
│   │   ├── setting.py
│   │   └── url.py
│   ├── db.py
│   └── main.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── .dockerignore
├── .gitignore
└── README.md
```

## Environment Variables

Create a `.env` file based on `.env.example`:

```env
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=url_shortener
DB_HOST=db
SALT=change_me
APP_PORT=8000
```

For Docker Compose, use:

```env
DB_HOST=db
```

For local development without Docker, use:

```env
DB_HOST=localhost
```

## Run with Docker Compose

Build and start the project:

```bash
docker compose up --build
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Stop containers:

```bash
docker compose down
```

If you need to remove local PostgreSQL data:

```bash
sudo rm -rf .pgdata
```

## API Endpoints

| Method | Endpoint            | Description                       |
| ------ | ------------------- | --------------------------------- |
| GET    | `/`                 | Check application status          |
| GET    | `/urls/health`      | Healthcheck endpoint              |
| POST   | `/urls/shorten`     | Create a short URL                |
| GET    | `/urls/`            | Get all shortened URLs            |
| GET    | `/urls/{short_url}` | Get information about a short URL |
| GET    | `/{short_url}`      | Redirect to the original URL      |
| PATCH  | `/urls/{short_url}` | Update the original URL           |
| DELETE | `/urls/{short_url}` | Delete a short URL                |

## Request Examples

### Create a short URL

```bash
curl -X POST http://127.0.0.1:8000/urls/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://roadmap.sh/python"}'
```

Example response:

```json
{
  "id": 1,
  "url": "https://roadmap.sh/python",
  "short_url": "abc123",
  "created_at": "2026-06-15T12:00:00",
  "updated_at": "2026-06-15T12:00:00",
  "clicks": 0
}
```

### Get URL information

```bash
curl http://127.0.0.1:8000/urls/abc123
```

Example response:

```json
{
  "id": 1,
  "url": "https://roadmap.sh/python",
  "short_url": "abc123",
  "created_at": "2026-06-15T12:00:00",
  "updated_at": "2026-06-15T12:00:00",
  "clicks": 0
}
```

### Redirect by short URL

Open in browser:

```text
http://127.0.0.1:8000/abc123
```

Or check with curl:

```bash
curl -I http://127.0.0.1:8000/abc123
```

After each redirect, the `clicks` counter is increased by 1.

### Update original URL

```bash
curl -X PATCH http://127.0.0.1:8000/urls/abc123 \
  -H "Content-Type: application/json" \
  -d '{"url": "https://fastapi.tiangolo.com/"}'
```

Example response:

```json
{
  "id": 1,
  "url": "https://fastapi.tiangolo.com/",
  "short_url": "abc123",
  "created_at": "2026-06-15T12:00:00",
  "updated_at": "2026-06-15T12:05:00",
  "clicks": 0
}
```

### Delete short URL

```bash
curl -X DELETE http://127.0.0.1:8000/urls/abc123
```

Example response:

```json
{
  "status": "Url deleted successful"
}
```

### Get all shortened URLs

```bash
curl http://127.0.0.1:8000/urls/
```

Example response:

```json
[
  {
    "url": "https://roadmap.sh/python",
    "short_url": "abc123"
  }
]
```

## Database

The project uses PostgreSQL as the database.

During development, PostgreSQL data is stored in the local `.pgdata/` directory. This directory is ignored by Git.

Currently, tables are created automatically with SQLAlchemy `create_all()` on application startup.

## Notes

The endpoint `GET /urls/` returns a list of all shortened URLs and is added for demonstration and testing purposes. In a real application, this endpoint should usually require authentication or pagination.

## Future Improvements

* Add Alembic migrations
* Add authentication and user accounts
* Add custom aliases for short URLs
* Add URL expiration dates
* Add pagination for the list endpoint
* Add tests with pytest
* Add rate limiting
* Improve validation with Pydantic `HttpUrl`
* Add deployment configuration

## Project Goal

This project was built as a learning backend project to practice:

* REST API design
* FastAPI routing
* PostgreSQL integration
* SQLAlchemy ORM
* Pydantic schemas
* Docker Compose
* Basic CRUD operations
* Redirect responses
* Simple click statistics

## Project URL

https://roadmap.sh/projects/url-shortening-service