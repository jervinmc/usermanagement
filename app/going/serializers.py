from rest_framework import serializers
from .models import Going

class GoingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Going
        fields="__all__"
