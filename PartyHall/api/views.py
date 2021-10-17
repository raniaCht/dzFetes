from rest_framework.generics import ListAPIView, RetrieveAPIView
from PartyHall.models import PartyHall
from .serializers import PartyHallSerializer

class PartyHallListView(ListAPIView):
    queryset = PartyHall.objects.all()
    serializer_class = PartyHallSerializer

class PartyHallDetailView(RetrieveAPIView):
    queryset = PartyHall.objects.all()
    serializer_class = PartyHallSerializer