from django.urls import path
from .views import PartyHallsView, PartyHallView, SearchView

urlpatterns = [
    path('', PartyHallsView.as_view()),
    path('search', SearchView.as_view()),
    path('<slug>', PartyHallView.as_view()),
]