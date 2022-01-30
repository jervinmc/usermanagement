from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Events
from .serializers import EventsSerializer
from rest_framework import filters
from rest_framework.response import Response
from datetime import datetime, timedelta
from users.models import User
from users.serializers import GetUserSerializer
class EventsView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Events.objects.all()
    serializer_class=EventsSerializer

    def list(self,request):
        if(self.request.user.is_superuser):
            items = Events.objects.all()
            items = EventsSerializer(items,many=True)
        else:
            items = Events.objects.filter(is_approved=True)
            items = EventsSerializer(items,many=True)
        for x in items.data:
            user = User.objects.filter(id=x['user_id'])
            user = GetUserSerializer(user,many=True)
            x['users']=user.data[0]
        # serializer = EventsSerializer(items,many=True)
        return Response(data=items.data)


class GetEventsByUserID(generics.GenericAPIView):
    def get(self,request,format=None):
        print(self.request.user.id)
        items = Events.objects.filter(user_id=self.request.user.id)
        serializer = EventsSerializer(items,many=True)
        return Response(data=serializer.data)

class UpcomingEvents(generics.GenericAPIView):
    def get(self,request,format=None):
        items = Events.objects.filter(event_start_date__lte=datetime.now()+timedelta(days=7),event_start_date__gte=datetime.now(),is_approved=True)
        serializer = EventsSerializer(items,many=True)
        for x in serializer.data:
            user = User.objects.filter(id=x['user_id'])
            user = GetUserSerializer(user,many=True)
            x['users']=user.data[0]
            print(user.data[0])
        # serializer = EventsSerializer(items,many=True)
        return Response(data=serializer.data)


class OfficialEvents(generics.GenericAPIView):
    def get(self,request,format=None):
        items = Events.objects.filter(event_type='official_event')
        serializer = EventsSerializer(items,many=True)
        for x in serializer.data:
            print(x)
            user = User.objects.filter(id=x['user_id'])
            user = GetUserSerializer(user,many=True)
            x['users']=user.data[0]
        # serializer = EventsSerializer(items,many=True)
        return Response(data=serializer.data)

class CommunityEvent(generics.GenericAPIView):
    def get(self,request,format=None):
        items = Events.objects.filter(event_type='community_led_event')
        serializer = EventsSerializer(items,many=True)
        for x in serializer.data:
            user = User.objects.filter(id=x['user_id'])
            user = GetUserSerializer(user,many=True)
            print(user.data[0])
            x['users']=user.data[0]
        # serializer = EventsSerializer(items,many=True)
        return Response(data=serializer.data)