from django.db import models

class PartyHall(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name