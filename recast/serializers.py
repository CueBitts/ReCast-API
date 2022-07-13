from rest_framework import serializers
from .models import Recast

class RecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recast
        fields = ['id', 'name']
