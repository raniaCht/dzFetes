from rest_framework import serializers
from PartyHall.models import PartyHall

class PartyHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyHall
        fields = ('id', 'name', 'address')