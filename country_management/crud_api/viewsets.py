from rest_framework import viewsets
from . import models
from . import serializers


# Adding Viewsets for Country and City
class CountryViewset(viewsets.ModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class CityViewset(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
