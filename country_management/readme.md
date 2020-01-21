##Country Management

### Description
##### Country and city managemengt API to create,update and delete 
##### country and city according to details

#Endpoints


Name          | Method        |               Endpoints                 |      Body            |
------------- | ------------- | --------------------------------------  | -------------------- |
Country       | POST          |  http://127.0.0.1:8000/api/country/     |    refer point1      |       
Country       | GET           |  http://127.0.0.1:8000/api/country/     |   None               |
Country       | PUT           |  http://127.0.0.1:8000/api/country/2/   |    refer point2      |
Country       | DELETE        |  http://127.0.0.1:8000/api/country/2/   |   None               |
City          | POST          |  http://127.0.0.1:8000/api/city/        |    refer point3      |
City          | GET           |  http://127.0.0.1:8000/api/city/        |   None               |
City          | PUT           |  http://127.0.0.1:8000/api/city/2/      |    refer point4      |
City          | DELETE        |  http://127.0.0.1:8000/api/city/2/      |   None               |
City          | GET           |  http://127.0.0.1:8000/api/search/      |   None               |

###point1
{
"country_name": "Australia",
"short_name": "Aus",
"country_code": 41
}

###point2
{
"country_name": "Australia",
"short_name": "Aust",
"country_code": 41
}

###point3
{
"country": 2,
"city_name": "sydney",
"city_code": 411
}

####Database
<!-- Please change credentials accordingly -->
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restfulapi',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost'


