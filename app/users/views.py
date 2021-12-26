from django.shortcuts import render
from rest_framework import viewsets
# from .models import User
from rest_framework.permissions import DjangoModelPermissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import email.message
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
import smtplib
import random
import string
from django.utils import timezone
from django.contrib.postgres.search import SearchVector
from decouple import config
from rest_framework import filters
from rest_framework import permissions
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string, get_template
from .models import User
from .serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissions, )
    queryset=User.objects.all()
    serializer_class=UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    @swagger_auto_schema(method="patch", request_body=UserSerializer)
    @action(detail=True, methods=["PATCH"])
    def update_users(self,request,pk=None):
        user=self.queryset.get(pk=pk)
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user_serializer=self.get_serializer(user,data=request.data)
        if not user_serializer.is_valid():
            # user_serializer.save()
            return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        unit_serializer.save()
        return Response(status=status.HTTP_200_OK,data=user_serializer.data)

    @swagger_auto_schema(method="patch", request_body=UserSerializer)
    @action(detail=True, methods=["PATCH"])
    def activate(self,request,pk=None):
        print(request.data)
        user=None
        try:
            user = User.objects.get(pk=pk)
            print(user)
            user_serializer=UserSerializer(user,data=request.data,partial=True)
            print(user.birthdate)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(data=user_serializer.data)
           
            return Response(data=user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get_search_results(self, view, request):
        return Response("none")
