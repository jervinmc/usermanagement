from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Announcement
from .serializers import AnnouncementSerializer
from rest_framework import filters
from rest_framework.response import Response

class AnnouncementView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','descriptions']
    queryset=Announcement.objects.all()
    serializer_class=AnnouncementSerializer
    def list(self,request):
        # if(self.request.user.is_superuser):
        items = Announcement.objects.all()
        # else:
        #     items = Announcement.objects.filter(is_active=True)
        serializer = AnnouncementSerializer(items,many=True)
        return Response(data=serializer.data)
