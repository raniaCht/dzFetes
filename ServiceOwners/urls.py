from django.urls import path
from .views import ServiceOwnerListView, ServiceOwnerView

urlpatterns = [
    path('', ServiceOwnerListView.as_view()),
    path('<pk>', ServiceOwnerView.as_view()),
]