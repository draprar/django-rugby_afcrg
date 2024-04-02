# Django-rugby Web App

This project is a web app developed for learning purposes, which is basically rewritten from an old website written in HTML and CSS into a web-app using the Django framework and python programming.
Check it: https://rugby.fly.dev/

## Technologies

- Python 3.10 as the programming language
- Django 4.1.3 as the web framework
- PostgreSQL 16.1 as the database
- HTML, CSS, and JavaScript as the web languages
- Bootstrap 5 as the front-end framework

## Installation

If you really want to install this project - write to me first to get the static files that I have not added here :) then follow these steps:

1. Clone this repository to your local machine.
2. Create and activate a virtual environment using pipenv or virtualenv.
3. Install the required packages using `pip install -r requirements.txt`.
4. Create your own .env file to hold secrets (SECRET_KEY, DEBUG state and DB) or edit settings.py file.
5. Run `python manage.py migrate` to create the database tables.
6. Run `python manage.py runserver` to start the development server.

## Usage

To use this project, open your browser and go to `http://127.0.0.1:8000/`. You should see the home page of the web app, which displays an archive page of a rugby team from Giżycko, Poland.
