from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Marketplace
from .serializers import MarketplaceSerializer
from rest_framework import filters
import json
from rest_framework.response import Response
from users.models import User
from users.serializers import GetUserSerializer
import requests
class MarketplaceView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Marketplace.objects.all()
    serializer_class=MarketplaceSerializer

    def list(self,request):
        items = Marketplace.objects.all()
        items = self.filter_queryset(items)
        items = MarketplaceSerializer(items,many=True)
        items_all = []
        for x in items.data:
            user = User.objects.filter(id=x['user_id'])
            user = GetUserSerializer(user,many=True)
            x['users']=user.data[0]
            # x['email']=user.data[0]['email']
            # x['user_image']=user.data[0]['image']
        print(items.data)
        return Response(data=items.data)

class GetMarketplaceByUserID(generics.GenericAPIView):
    def get(self,request,format=None):
        items = Marketplace.objects.filter(user_id=self.request.user.id)
        serializer = MarketplaceSerializer(items,many=True)
        return Response(data=serializer.data)


class BuyPaymaya(generics.GenericAPIView):
    def post(self,request,format=None):
        res = request.data
        url = "https://pg-sandbox.paymaya.com/checkout/v1/checkouts"
        payload = {
            "totalAmount": {
                "value": res.get('price'),
                "currency": "PHP"
            },
            "buyer": {
                "billingAddress": {"countryCode": "GB"},
                "shippingAddress": {"countryCode": "GB"},
                "firstName": "Juan",
                "middleName": "D",
                "lastName": "Delacruz",
                "birthday": "2019-10-19"
            },
            "items": [
                {
                    "amount": {"value": res.get('price')},
                    "totalAmount": {"value": res.get('price')},
                    "name": res.get('product'),
                    "quantity": "1",
                    "code": "uus",
                    "description": "dse"
                }
            ],
            "requestReferenceNumber": "123123"
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Basic cGstWjBPU3pMdkljT0kyVUl2RGhkVEdWVmZSU1NlaUdTdG5jZXF3VUU3bjBBaDo="
        }

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return Response(data=response.text)


