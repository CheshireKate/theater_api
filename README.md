# Theater API Service

A RESTful API for managing a theater ticket reservation system, built with Django REST Framework.

## Features

* User registration and authentication (via JWT)
* View and manage plays, genres, actors, theater halls, performances
* Reserve and purchase tickets
* Admin panel for full management access
* Dockerized setup for easy deployment

## Tech Stack

* Python 3.11+
* Django 4.x
* Django REST Framework
* PostgreSQL
* Docker & Docker Compose
* JWT authentication (`djangorestframework-simplejwt`)

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd theater_api_service
```

### 2. Create `.env` file

Use the provided `.env sample` to create your `.env`:

```bash
cp .env\ sample .env
```

Set up environment variables as needed (DB credentials, secret key, etc.).

### 3. Run with Docker

```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`.

### 4. Run migrations and create superuser

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### 5. Access admin panel

Visit `http://localhost:8000/admin/` and log in with your superuser credentials.

## API Endpoints

### Authentication

* `POST /api/user/create/` – Register a new user
* `POST /api/token/` – Get JWT token
* `POST /api/token/refresh/` – Refresh token
* `GET /api/user/manage/` – Retrieve or update current user

### Theater Functionality

Assuming routes are defined in `theater/urls.py`. Examples:

* `GET /api/plays/`
* `GET /api/performances/`
* `POST /api/reservations/`
* `POST /api/tickets/`

## Project Structure

```
theater_api_service/
├── theater/                 # Main app for theater-related models and logic
├── user/                    # Custom user management
├── theater_api_service/     # Project settings
├── docker-compose.yml
├── Dockerfile
├── .env
├── requirements.txt
└── manage.py
```

## Development

Install dependencies locally:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
python manage.py runserver
```
