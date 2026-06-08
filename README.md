# 🚀 Django Portfolio — Setup Guide

## Prerequisites
- Python 3.10+
- pip

---

## Quick Start

```bash
# 1. Enter project folder
cd portfolio

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Create superuser (for admin panel)
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver
```

Then open: http://127.0.0.1:8000

Admin panel: http://127.0.0.1:8000/admin/

---

## 📁 Project Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── portfolio/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                # Main app
│   ├── models.py        # Project, Skill, ContactMessage models
│   ├── views.py         # Home, About, Projects, Contact views
│   ├── forms.py         # Contact form
│   ├── admin.py         # Admin configuration
│   └── urls.py
├── templates/           # HTML templates
│   ├── base.html        # Navbar + Footer
│   ├── home.html        # Home page
│   ├── about.html       # About page
│   ├── contact.html     # Contact page
│   └── projects.html    # Projects page
└── static/
    ├── css/style.css    # All styles
    └── js/main.js       # All JavaScript
```

---

## ✏️ Personalizing

1. **Your Name** — Search and replace `Your Name` in all templates
2. **Email** — Update `your@email.com` in templates and contact info
3. **Social links** — Update GitHub/LinkedIn URLs in `base.html`
4. **Location** — Update Surat references if needed
5. **Skills/Projects** — Add via Django admin panel at `/admin/`

---

## 🔧 Adding Content via Admin

1. Go to http://127.0.0.1:8000/admin/
2. **Skills** → Add your skills with name, category, proficiency (0–100), icon (emoji)
3. **Projects** → Add projects with title, description, tech stack, GitHub/live URLs
4. **Contact Messages** → View messages sent via the contact form

### Skill Categories:
- `language` — Programming Languages (Python, JS, SQL…)
- `framework` — Frameworks (Django, React…)
- `data` — Data Science tools
- `tool` — Dev tools (Git, Docker…)

---

## 🚀 Production Deployment

For production, update `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = 'use-a-secure-random-key'
```

Use whitenoise for static files and gunicorn as the WSGI server.

---

## 📦 Future Additions (Scalable)

The app is designed to scale. You can easily add:
- Blog app (`python manage.py startapp blog`)
- Portfolio detail pages
- Image gallery
- Testimonials app
- Resume/CV download
- Dark/Light mode toggle
- i18n (translations)
