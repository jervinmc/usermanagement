from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Discussionspace
from .serializers import DiscussionspaceSerializer
from rest_framework import filters

class DiscussionspaceView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','descriptions']
    queryset=Discussionspace.objects.all()
    serializer_class=DiscussionspaceSerializer
