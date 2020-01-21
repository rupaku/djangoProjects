from .models import Country, City
from django.shortcuts import render
from .filters import CountryFilter, CityFilter


# Function to search according to country_code and city_code
def search(request):
    country_list = Country.objects.all()
    country_filter = CountryFilter(request.GET, queryset=country_list)
    return render(request, 'templates/input_list.html', {'filter': country_filter})
