from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import PartyHall
from .serializers import PartyHallSerializer, PartyHallDetailSerializer
from datetime import datetime, timezone, timedelta

class PartyHallsView(ListAPIView):
    queryset = PartyHall.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = PartyHallSerializer
    lookup_field = 'slug'

class PartyHallView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = PartyHall.objects.all()
    serializer_class = PartyHallDetailSerializer
    lookup_field = 'slug'

class SearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = PartyHallSerializer

    def post(self, request, format=None):
        queryset = PartyHall.objects.all()
        data = self.request.data

        city = data['city']
        queryset = queryset.filter(city__iexact=city)

        price = data['price']
        if price == '$0+':
            price = 0
        elif price == '$200,000+':
            price = 200000
        elif price == '$400,000+':
            price = 400000
        elif price == '$600,000+':
            price = 600000
        elif price == '$800,000+':
            price = 800000
        elif price == '$1,000,000+':
            price = 1000000
        elif price == '$1,200,000+':
            price = 1200000
        elif price == '$1,500,000+':
            price = 1500000
        elif price == 'Any':
            price = -1
        
        if price != -1:
            queryset = queryset.filter(price__gte=price)

        title = data['title']
        queryset = queryset.filter(title__iexact=title)

        nbrPlace = data['nbrPlace']
        if nbrPlace == '1000+':
            nbrPlace = 1000
        elif nbrPlace == '1200+':
            nbrPlace = 1200
        elif nbrPlace == '1500+':
            nbrPlace = 1500
        elif nbrPlace == '2000+':
            nbrPlace = 2000
        elif nbrPlace == 'Any':
            nbrPlace = 0
        
        if nbrPlace != 0:
            queryset = queryset.filter(nbrPlace__gte=nbrPlace)

        keywords = data['keywords']
        queryset = queryset.filter(description__icontains=keywords)

        serializer = PartyHallSerializer(queryset, many=True)

        return Response(serializer.data)