from django.db import models


# Create Country and City Model with fields details
class Country(models.Model):
    country_name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=5, unique=True)
    country_code = models.IntegerField(unique=True)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=20)
    city_code = models.IntegerField(unique=True)
