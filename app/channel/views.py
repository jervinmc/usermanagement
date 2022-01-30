from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Channel
from .serializers import ChannelSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
from chat.models import Chat
from chat.serializers import ChatSerializer
import pusher
from decouple import config 
pusher_client = pusher.Pusher(
  app_id=config('APP_ID'),
  key=config('PUSHER_KEY'),
  secret=config('SECRET_KEY'),
  cluster='ap1',
  ssl=True
)
class ChannelView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Channel.objects.all()
    serializer_class=ChannelSerializer
    def list(self,request,format=None,email=None):
        try:
            if True:
                items = Channel.objects.filter(seller_id=self.request.user.id) | Channel.objects.filter(customer_id=self.request.user.id) 
                items = ChannelSerializer(items,many=True)
                for x in items.data:
                    user = User.objects.filter(id=x['customer_id'])
                    user = GetUserSerializer(user,many=True)
                    x['users']=user.data[0]
            elif self.request.user.account_type=='Customer':
                items = Channel.objects.filter(customer_id=self.request.user.id)
                items = ChannelSerializer(items,many=True)
                for x in items.data:
                    user = User.objects.filter(id=x['seller_id'])
                    user = GetUserSerializer(user,many=True)
                    x['users']=user.data[0]
            return Response(status=status.HTTP_200_OK,data=items.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

class ChannelSend(generics.GenericAPIView):
    queryset=Channel.objects.all()
    serializer_class=ChannelSerializer
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        pusher_client.trigger(request.data.get('channel'), 'my-test', {'message': request.data.get('message')})
        serializer = ChatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()

