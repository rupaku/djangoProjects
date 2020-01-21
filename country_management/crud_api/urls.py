from django.conf.urls import url
from crud_api.search import views

# Adding endpoint for Filteration
urlpatterns = [
    url(r'^search/$', views.search, name='search'),
]