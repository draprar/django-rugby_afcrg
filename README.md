![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-4.2+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 🏉 AFC Rugby Giżycko — Django App (Archived)

A Django rebuild of the original AFC Rugby Giżycko static website.
Transformed from a simple HTML/CSS site into a dynamic web application with backend logic and database support.

> ⚠️ This repository is archived.  
> Originally rebuilt from a static HTML version:  
> https://github.com/draprar/html-rugby  
>
> And is now part of my main portfolio:  
> https://github.com/draprar/django_portfolio-walery (see `/rugby` app)

> 🌐 Live version: https://walery.site/rugby/

![Project Demo](archive/static/assets/demo.gif)

## 📖 Overview

This project is a Django-based rebuild of the original AFC Rugby Giżycko static website.
It was created as a learning exercise to transform a simple HTML/CSS site into a dynamic web application with backend logic and database support.
The project was later integrated into a larger modular portfolio system.

## 🧠 Project Evolution

- Static HTML/CSS website
- Rebuilt as a Django application (this repository)  
- Integrated into the portfolio project as a module
- Archived for historical reference
 
## ✨ Features

- **Dynamic Content Management**
  - Backend-driven pages replacing static HTML
- **Database Support**
  - MySQL integration for structured data
- **Responsive Design**
  - Built with Bootstrap for desktop and mobile views

## 🚀 Installation

### Requirements

- Python 3.10+
- Django 4.2+
- MySQL
- Bootstrap (frontend)

### Step-by-Step Guide

1. **Clone the repository**:
```
   git clone https://github.com/draprar/django-rugby_afcrg.git
   cd django-rugby_afcrg
```

2. **Create and activate a virtual environment**:
```
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```
   pip install -r requirements.txt
```

4. **Set up environment variables** (optional):
```
   touch .env
```

5. **Apply migrations**:
```
   python manage.py makemigrations
   python manage.py migrate
```

8. **Run the development server**:
```
   python manage.py runserver
```

9. **Access the application**:
   - Main page: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📜 License

This project is licensed under the MIT License.

## 👤 Author

Developed by Walery ([@draprar](https://github.com/draprar/)).
