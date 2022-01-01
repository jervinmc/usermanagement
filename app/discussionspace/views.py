from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Discussionspace
from .serializers import DiscussionspaceSerializer
from rest_framework import filters
from rest_framework import viewsets,generics
from rest_framework.response import Response
class DiscussionspaceView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','descriptions']
    queryset=Discussionspace.objects.all()
    serializer_class=DiscussionspaceSerializer

class GetDiscussionsByUserID(generics.GenericAPIView):
    def get(self,request,format=None):
        items = Discussionspace.objects.filter(user_id=self.request.user.id)
        serializer = DiscussionspaceSerializer(items,many=True)
        return Response(data=serializer.data)