# 🏉 AFC Rugby Giżycko — Django App (Archived)

> ⚠️ This repository is archived.  
> Originally rebuilt from a static HTML version:  
> https://github.com/draprar/html-rugby  
>
> And is now part of my main portfolio:  
> https://github.com/draprar/django_portfolio-walery (see `/rugby` app)

![Project Demo](archive/static/assets/demo.gif)

## 📖 Overview
This project is a Django-based rebuild of the original AFC Rugby Giżycko static website.

It was created as a learning exercise to transform a simple HTML/CSS site into a dynamic web application with backend logic and database support.  
The project was later integrated into a larger modular portfolio system.

## 🧠 Project Evolution
- Static HTML/CSS website → https://github.com/draprar/html-rugby  
- Rebuilt as a Django application (this repository)  
- Integrated into a modular Django portfolio → https://github.com/draprar/django_portfolio-walery
  
## 🛠️ Technology Stack

- **Backend**: Python 3.10, Django
- **Database**: MySQL
- **Frontend**: HTML, CSS, Bootstrap, JavaScript

## 🚀 Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/draprar/django-rugby_afcrg.git
   cd django-rugby_afcrg
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   
4. (optional) Create your own .env file for environment variables:
   ```bash
   touch .env
   ```

5. Apply migrations;
   ```bash
   python manage.py migrate
   python manage.py makemigrations
   ```

6. Collect static files (for production):
   ```bash
   python manage.py collectstatic
   ```

7. Run the development server:
    ```bash
   python manage.py runserver
   ```

## 📌 **Notes**
- This project is no longer actively maintained
- Serves as a standalone version of the Rugby app before integration
- Demonstrates transition from static frontend to full Django stack

## 👤 **Author**

- **Built by**: Walery ([@draprar](https://github.com/draprar/))
