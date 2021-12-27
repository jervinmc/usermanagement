from rest_framework import serializers
from .models import Discussionspace

class DiscussionspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Discussionspace
        fields="__all__"
