# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.symbol} - {self.name}"
        


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username}'s Watchlist - {self.symbol}"

