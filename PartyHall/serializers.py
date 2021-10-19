from rest_framework import serializers
from .models import PartyHall

class PartyHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyHall
        fields = ('title', 'address', 'city', 'price', 'nbrPlace', 'photo_main', 'slug')

class PartyHallDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyHall
        fields = '__all__'
        lookup_field = 'slug'