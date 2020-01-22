## Country Management

### Description
Country and city management API to create,update and delete country and city according to details

### Requirement
django-admin startproject country_management
cd country_management
python manage.py startapp crud_api
pip install djangorestframework
install postgresql on your system
pip install psycopg2
pip install django-filter
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

### Endpoints

Name          | Method        |               Endpoints                 |      Body            |
------------- | ------------- | --------------------------------------  | -------------------- |
Country       | POST          |  http://127.0.0.1:8000/api/country/     |   refer dataset 1    |       
Country       | GET           |  http://127.0.0.1:8000/api/country/     |   None               |
Country       | PUT           |  http://127.0.0.1:8000/api/country/2/   |   refer dataset 2    |
Country       | DELETE        |  http://127.0.0.1:8000/api/country/2/   |   None               |
City          | POST          |  http://127.0.0.1:8000/api/city/        |   refer dataset 3    |
City          | GET           |  http://127.0.0.1:8000/api/city/        |   None               |
City          | PUT           |  http://127.0.0.1:8000/api/city/2/      |   refer dataset 4    |
City          | DELETE        |  http://127.0.0.1:8000/api/city/2/      |   None               |
City          | GET           |  http://127.0.0.1:8000/api/search/      |   None               |

### Dataset 1:
    {
    "country_name": "Australia",
    "short_name": "Aus",
    "country_code": 41
    }

### Dataset 2:
    {
    "country_name": "Australia",
    "short_name": "Aust",
    "country_code": 41
    }

### Dataset 3:
    {
    "country": 2,
    "city_name": "sydney",
    "city_code": 411
    }

### Dataset 4:
    {
    "country": 2,
    "city_name": "canberra",
    "city_code": 411
    }

### Database:
<!-- Please change credentials accordingly -->
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restfulapi',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost'


