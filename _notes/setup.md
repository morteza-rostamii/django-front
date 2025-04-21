<!--

py -m venv .venv

source .venv/Scripts/activate

pip install django

django-admin startproject myproject .

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

nomad
pass: 12345678

python manage.py startapp myapp

myproject/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Add this
]

# hot reload

https://medium.com/@appseed.us/django-hot-reload-templates-and-static-4d74a774b26f
python manage.py runserver

# compile assets on production (static folder)
Run python manage.py collectstatic if deploying

# buy default it submits the form to the same route that renders the form

# explicitly set the form action to the route that handles the form
<form method="post" action="{% url 'task_create' %}">


# fix tailwindcss intellisense
https://www.youtube.com/watch?v=fODz-vDkEac


pip freeze > requirements.txt

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

 -->
