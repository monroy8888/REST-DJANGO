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

-------------------------------------

$ sudo emacs lib/python3.7/site-packages/pgadmin4/config_local.py

add :

import os
DATA_DIR = os.path.realpath(os.path.expanduser(u'~/.pgadmin/'))
LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')
SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin4.db')
SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions')
STORAGE_DIR = os.path.join(DATA_DIR, 'storage')
SERVER_MODE = False
DEFAULT_SERVER = '0.0.0.0'
DEFAULT_SERVER_PORT = 5050




$ python lib/python3.7/site-packages/pgadmin4/pgAdmin4.py


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

7) Run server and test

- python3 manage.py runserver
- check the url 127.0.0.1

------------------------------------------------

8) Create app api and add model
- Make migrations
- migrate
- test in the python3 manage.py shell
---------------
ADD:
    Categoria.objects.bulk_create([
    Categoria(descripcion='Informática'),
    Categoria(descripcion='Matemáticas'),
    Categoria(descripcion='Inglés'),
    Categoria(descripcion='Español'),
    Categoria(descripcion='Medicina'),
    ])

    Categoria.objects.all()
    Categoria.objects.all().values('id','descripcion')


    SubCategoria.objects.bulk_create([
    SubCategoria(categoria_id=1,descripcion='Desarrollo Web'),
    SubCategoria(categoria_id=1,descripcion='Base de Datos'),
    SubCategoria(categoria_id=1,descripcion='Desarrollo Desktop'),
    SubCategoria(categoria_id=1,descripcion='FrameWorks'),
    SubCategoria(categoria_id=2,descripcion='Algebra'),
    SubCategoria(categoria_id=2,descripcion='Análisis Numéricos'),
    SubCategoria(categoria_id=3,descripcion='Principiante'),
    SubCategoria(categoria_id=3,descripcion='Avanzado'),
    ])

----------------------------------------
    #Entramos en el shell de Django 
    manage.py shell

    from api.serializers import ProductoSerializer
    from api.models import Producto


    prod_serializer = ProductoSerializer(data={"subcategoria":1,"descripcion":"Desarrollo Web con Python usando Django 2.1","fecha_creado":"2018-10-01T12:11:37.090335Z"})
    prod_serializer.is_valid()
    prod1 = prod_serializer.save()
    prod1.pk

        prod_serializer = ProductoSerializer(instance=prod1, data={"subcategoria":1,"descripcion":"Desarrollo Web con Python usando Django","fecha_creado":"2018-10-01T12:11:37.090335Z"})
    prod_serializer.is_valid()
    prod_serializer.save()

        prod1 = Producto.objects.all().first()
    prod_serializer1 = ProductoSerializer(prod1)
    prod_serializer1.data

    prod2 = ProductoSerializer(Producto.objects.all(),many=True)
    prod2.data

    ------------------------------------------------------------

        http://127.0.0.1:8000/api/v1/productos/
    http://127.0.0.1:8000/api/v1/productos/1


    Producto.objects.bulk_create([
    Producto(subcategoria_id=2,descripcion='Replicacion de Base de Datos con SymmetricDS',fecha_creado='2018-11-01T12:11:37.090335Z'),
    Producto(subcategoria_id=3,descripcion='Desarrollo de Aplicaciones en Capas',fecha_creado='2017-08-01T12:11:37.090335Z'),
    Producto(subcategoria_id=4,descripcion='Domina ORM de Django',fecha_creado='2019-01-04T12:11:37.090335Z'),
    Producto(subcategoria_id=4,descripcion='Introducción a Entity FrameWork',fecha_creado='2017-08-05T12:11:37.090335Z'),
    Producto(subcategoria_id=5,descripcion='Álgebra Baldor',fecha_creado='2015-05-05T12:11:37.090335Z'),
    ])

    ----------------------------------------------------------

    
    
