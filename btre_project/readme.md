### virtual env
python -m venv ./venv
activate
pip freeze 
pip install django

### create project
django-admin startproject btre

### create app inside project
python manage.py startapp pages
### init repo project
git init
.gitignoregit

### settings.py -> INSTALLED_APPS
 'pages',
 
 ### static
 python manage.py collectstatic
 
 {% load static %} in base.html


## apps
python manage.py startapp listings
python manage.py startapp realtors

##endpoints
/listings/

