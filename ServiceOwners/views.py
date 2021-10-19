from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import ServiceOwner
from .serializers import ServiceOwnerSerializer

class ServiceOwnerListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = ServiceOwner.objects.all()
    serializer_class = ServiceOwnerSerializer
    pagination_class = None

class ServiceOwnerView(RetrieveAPIView):
    queryset = ServiceOwner.objects.all()
    serializer_class = ServiceOwnerSerializer