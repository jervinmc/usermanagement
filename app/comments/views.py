from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Comments
from .serializers import CommentsSerializer
from rest_framework import filters
from rest_framework import viewsets,generics
from rest_framework.response import Response
from users.models import User
from users.serializers import GetUserSerializer
class CommentsView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','descriptions']
    queryset=Comments.objects.all()
    serializer_class=CommentsSerializer
    # def list(self,request):
    #     items = Comments.objects.all()
    #     items = self.filter_queryset(items)
    #     items = CommentsSerializer(items,many=True)
    #     items_all = []
    #     for x in items.data:
    #         user = User.objects.filter(id=x['user_id'])
    #         user = GetUserSerializer(user,many=True)
    #         x['users']=user.data[0]
    #         # x['email']=user.data[0]['email']
    #         # x['user_image']=user.data[0]['image']
    #     print(items.data)
    #     return Response(data=items.data)  

# class GetDiscussionsByUserID(generics.GenericAPIView):
#     def get(self,request,format=None):
#         items = Comments.objects.filter(user_id=self.request.user.id)
#         serializer = CommentsSerializer(items,many=True)
#         return Response(data=serializer.data)


class CommentsDiscussion(generics.GenericAPIView):
    def post(self,request,format=None):
        items = Comments.objects.filter(discussion_id=request.data.get('id'))
        serializer = CommentsSerializer(items,many=True)
        return Response(data=serializer.data)