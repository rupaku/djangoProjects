from django.shortcuts import render
from rest_framework import viewsets,filters
from .serializers import StockSerializer,UserSerializer
from .models import Stock
from restapp import views
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

# Create your views here.
class StockViewSet(viewsets.ModelViewSet):
    '''to sort acc to stcok_gain'''
    '''queryset=Stock.objects.all().order_by('stock_gain')'''
    permission_classes=(IsAuthenticated,)
    queryset=Stock.objects.all()
    serializer_class=StockSerializer
    filter_backends=(DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields=('market_name',)
    search_fields=('stock_name',)
    ordering=('stock_gain',)
class CreateUserView(CreateAPIView):
    model=get_user_model()
    permission_classes=(AllowAny,)
    serializer_class=UserSerializer
