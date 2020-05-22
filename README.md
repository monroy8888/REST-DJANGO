# REST-DJANGO
Step by Step
------------------------

1) To Set the environment to work:

- install env
- source my_env/bin/activate
- deactive...
--------------------------------
- install inside:
- pip install django
- pip install djangorestframework
- pip install psycopg2
- apt install curl
- pip install --upgrad httpie
- sudo snap install postman
- install postgrespsql

------------------------------------
Get into the db postgres and create a table:

- psql -U sergioq7777 -h 127.0.0.1 -p 5432 -d postgres

- or

- sudo -su
- su - postgres
- psql

- set de password
---------------------------------------------
CREATE DATABASE drf_api
- \l = to list
-----------------------------------------
env-directory:

- django-admin startproject djapi 

- go settings and add 'rest_framework' and the db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'drf_api',
        'HOST': '127.0.0.1',
        'USER': 'postgres',
        'PASSWORD': '!Andres!.88'
        'PORT': '5432',
    }
}
------------------------------------------------
- python3 manage.py migrate

To watch if it migrates ok !!
- python3 manage.py dbshell = to go directly to the db

-To watch insde the postgres db = \dt 

--------------------------------------

2) Start a new app "dj_puro":

- django-admin startapp dj_puro

-Add the requirements in settings.py

- INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'dj_puro',
]

3) Create model api in models.py:


- go to models and create it.
-python3 manage.py migrate
- then : python3 manage.py makemigrations
- To what what its missing : python3 manage.py showmigration

4) Connect Urls to views:

- Open views on dj_puro
- Edit URL
- Create urls.py on dj_puro

5) Creating views:
- Go into the app views.
- The views that we want to get are based on the models.

6)Fullfil tables into the "python3 manage.py shell" to watch the result:
- from dj_puro.models import Categoria
>>> Categoria.objects.bulk_create([
... Categoria(descripcion='Desarrollo web django',activo=False),
... Categoria(descripcion='Replicacion con sysmmetricsDS',activo=True),
... Categoria(descripcion='Domina ORM de Django',activo=True),
... Categoria(descripcion='Restful Api con Django Framework',activo=False),
... Categoria(descripcion='Administracion PostgreSQL',activo=True),
... ])
