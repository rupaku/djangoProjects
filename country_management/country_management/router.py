from crud_api.viewsets import CountryViewset, CityViewset
from rest_framework import routers

# Include country and city API endpoints
router = routers.DefaultRouter()
router.register('country', CountryViewset)
router.register('city', CityViewset)

