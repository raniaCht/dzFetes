from rest_framework import serializers
from .models import ServiceOwner

class ServiceOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOwner
        fields = '__all__'