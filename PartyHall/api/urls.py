from django.urls import path
from .views import PartyHallListView, PartyHallDetailView

urlpatterns = [
    path('', PartyHallListView.as_view()),
    path('<pk>', PartyHallDetailView.as_view())
]