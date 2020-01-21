from django.contrib.auth.models import Country, City
import django_filters


# Adding Filters for Country and City according to country_code and city_code
class CountryFilter(django_filters.FilterSet):
    class Meta:
        model = Country
        fields = ['country_code']


class CityFilter(django_filters.FilterSet):
    class Meta:
        model = City
        fields = ['city_code']
