from rest_framework import serializers
from .models import Watchlist, Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock #Watchlist
        fields = ['id', 'symbol','name']
