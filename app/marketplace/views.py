from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Marketplace
from .serializers import MarketplaceSerializer
from rest_framework import filters

class MarketplaceView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Marketplace.objects.all()
    serializer_class=MarketplaceSerializer
