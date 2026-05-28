# 🌍 Hello Django — Python Django + PostgreSQL Starter

A clean, minimal **Hello World** project built with **Django 4.2** and **PostgreSQL**, ready for deployment.

---

## 🛠️ Tech Stack

| Layer      | Technology          |
|------------|---------------------|
| Language   | Python 3.11         |
| Framework  | Django 4.2          |
| Database   | PostgreSQL          |
| Config     | python-decouple     |
| Server     | Gunicorn (prod)     |

---

## 📁 Project Structure

```
hello_django/
├── hello_django/          # Django project config
│   ├── __init__.py
│   ├── settings.py        # Settings (reads from .env)
│   ├── urls.py            # Root URL config
│   ├── wsgi.py
│   └── asgi.py
├── hello/                 # Hello World app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # Message model (stored in PostgreSQL)
│   ├── urls.py
│   └── views.py
├── templates/
│   └── hello/
│       └── index.html     # Hello World HTML page
├── manage.py
├── requirements.txt
├── .env                   # ⚠️ NOT committed to git
├── .env.example           # ✅ Safe to commit
└── .gitignore
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd hello_django
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
# Copy the example env file
copy .env.example .env     # Windows
cp .env.example .env       # macOS / Linux

# Edit .env with your database credentials
```

Your `.env` should look like:

```env
SECRET_KEY=your-very-secret-key-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=hello_django_db
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Create the PostgreSQL Database

```sql
-- In psql shell:
CREATE DATABASE hello_django_db;
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser at **http://127.0.0.1:8000/** 🎉

---

## 🔗 Available Endpoints

| URL            | Description                          |
|----------------|--------------------------------------|
| `/`            | Hello World HTML page                |
| `/health/`     | JSON health check (DB status)        |
| `/admin/`      | Django Admin Panel                   |

---

## 🌐 Deployment

### Using Gunicorn

```bash
gunicorn hello_django.wsgi:application --bind 0.0.0.0:8000
```

### Production Checklist

- [ ] Set `DEBUG=False` in `.env`
- [ ] Set a strong `SECRET_KEY`
- [ ] Add your domain to `ALLOWED_HOSTS`
- [ ] Set up Nginx as a reverse proxy
- [ ] Collect static files: `python manage.py collectstatic`
- [ ] Use a process manager (e.g., systemd or supervisor)

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 📄 License

MIT License — free to use and modify.
