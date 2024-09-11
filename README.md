# AFC Rugby Giżycko Archive - Website

![Project Demo](static/assets/demo.gif)

This project is a web app developed for learning purposes, which is basically rewritten from an old website written in HTML and CSS into a web-app using the Django framework and python programming.
Check it: https://afcrg.pythonanywhere.com/

## Technology Stack

- **Backend**: Python 3.10, Django
- **Database**: MySQL
- **Frontend**: HTML, CSS, Bootstrap, JavaScript

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/draprar/django-rugby.git
   cd django-rugby
   ```

2. Create and activate a virtual environment
   ```bash
   virtualenv venv
   source venv/bin/activate
   ```

3. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```
   
4. Create your own .env file to hold secrets or edit settings.py file
   ```bash
   touch .env
   ```

5. Apply database migrations
   ```bash
   python manage.py migrate
   python manage.py makemigrations
   ```

6. Collect static files (for production environments)
   ```bash
   python manage.py collectstatic
   ```

7. Start the development server
    ```bash
   python manage.py runserver
   ```

## **Credits**

- **Developer**: Walery ([@draprar](https://github.com/draprar/))