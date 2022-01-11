from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Discussionspace
from .serializers import DiscussionspaceSerializer
from rest_framework import filters
from rest_framework import viewsets,generics
from rest_framework.response import Response
from users.models import User
from users.serializers import GetUserSerializer
class DiscussionspaceView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','descriptions']
    queryset=Discussionspace.objects.all()
    serializer_class=DiscussionspaceSerializer
    def list(self,request):
        items = Discussionspace.objects.all()
        items = self.filter_queryset(items)
        items = DiscussionspaceSerializer(items,many=True)
        items_all = []
        for x in items.data:
            user = User.objects.filter(id=x['user_id'])
            user = GetUserSerializer(user,many=True)
            x['users']=user.data[0]
            # x['email']=user.data[0]['email']
            # x['user_image']=user.data[0]['image']
        print(items.data)
        return Response(data=items.data)  

class GetDiscussionsByUserID(generics.GenericAPIView):
    def get(self,request,format=None):
        items = Discussionspace.objects.filter(user_id=self.request.user.id)
        serializer = DiscussionspaceSerializer(items,many=True)
        return Response(data=serializer.data)