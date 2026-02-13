# Ross' Rotisserie Website

This site now runs on Django, with the original multi-page layout converted into server-rendered templates and a reviews page backed by a database model.

## Pages
- Home: Highlights the menu and testimonials.
- Menu: Detailed offerings and an order form.
- About: Team, story, and contact form.
- Reviews: Database-backed customer reviews.

## Features
- Shared layout and navigation/footer includes via Django templates.
- Reviews stored in a SQLite database and managed via Django admin.
- Responsive layout with mobile-friendly navigation.
- Google Fonts for brand-appropriate typography.
- Accessible focus states and skip-to-content link.

## Structure
- ross_rotisserie/: Django project settings.
- core/: Django app with views and the Review model.
- templates/: Django templates (pages + partials).
- static/: Global styling.

## Run locally
1) Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Run migrations and create an admin user:

```bash
python manage.py migrate
python manage.py createsuperuser
```

3) Start the dev server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site and `http://127.0.0.1:8000/admin/` to manage reviews.