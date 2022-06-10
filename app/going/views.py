from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Going
from .serializers import GoingSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class GoingView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Going.objects.all()
    serializer_class=GoingSerializer




class GoingUser(generics.GenericAPIView):
    def post(self,request,format=None):
        res = request.data
        item = Going.objects.filter(user_id=res.get('user_id'),event_id=res.get('event_id')).count()
        if(len(item)!=0):
            return Response(data=False)

        else:
            return Response(data=True)
        
