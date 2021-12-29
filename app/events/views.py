from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Events
from .serializers import EventsSerializer
from rest_framework import filters
from rest_framework.response import Response

class EventsView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Events.objects.all()
    serializer_class=EventsSerializer

    def list(self,request):
        if(self.request.user.is_superuser):
            items = Events.objects.all()
        else:
            items = Events.objects.filter(is_approved=True)
        serializer = EventsSerializer(items,many=True)
        return Response(data=serializer.data)