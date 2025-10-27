from rest_framework import serializers
from .models import Coders

class CoderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coders
        fields="__all__"