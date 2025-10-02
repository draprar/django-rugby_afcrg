# AFC Rugby Giżycko Archive

![Project Demo](archive/static/assets/demo.gif)

Once upon a time this was a plain HTML/CSS site. Now it’s reborn as a Django web app — because learning by rebuilding old stuff is fun.

## Technology Stack

- **Backend**: Python 3.10, Django
- **Database**: MySQL
- **Frontend**: HTML, CSS, Bootstrap, JavaScript

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/draprar/django-rugby_afcrg.git
   cd django-rugby_afcrg
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```
   
4. (optional) Create your own .env file to hold secrets or edit settings.py file
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

- **Built by**: Walery ([@draprar](https://github.com/draprar/))
