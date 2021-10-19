from django.contrib import admin
from .models import PartyHall

class PartyHallAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'serviceOwner')
    list_display_links = ('id', 'title')
    list_filter = ('serviceOwner', )
    search_fields = ('title', 'description', 'address', 'city', 'nbrPlace', 'price')
    list_per_page = 25

admin.site.register(PartyHall, PartyHallAdmin)