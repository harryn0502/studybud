# StudyBud
Django Practice Project

* Credit - https://github.com/divanov11/StudyBud

#

### App Setup

--> Move into the directory where we have the backend files : 
```bash
cd backend
```

--> Create a python virtual environment :
```bash
# Create a virtual environment
python venv [name]
```

--> Activate the virtual environment :
```bash
[name]\scripts\activate
```

--> If you want to deactivate the virtual environment :
```bash
[name]\scripts\deactivate
```

--> Install the requirements :
```bash
pip install -r requirements.txt
```

#

### Database Setup

--> Create a new database setup file:
```bash
python manage.py makemigrations
```

--> Next, create db.sqlite3 file:
```bash
python manage.py migrate
```

#

### Running the App

--> To run the App, use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/