from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('vrforms/',views.vrform,name='vrform')
]
