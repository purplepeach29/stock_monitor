# Create your views here.
from datetime import datetime
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Watchlist, Stock
from .serializers import StockSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import pip._vendor.requests
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print(username,password)
    user = authenticate(username=username, password=password)
    if user is not None:
        #token, _ = Token.objects.get_or_create(user=user)
        return Response({'msg': 'login success'})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)


@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    print(username)
    password = request.data.get('password')
    if not username or not password:
        return JsonResponse({'error': 'Username and password are required'}, status=400)
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username is already taken'}, status=400)
    user = User.objects.create_user(username=username, password=password)
    return JsonResponse({'message': 'User created successfully'})

class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

@api_view(['POST'])
def add_stock(request):
    serializer = StockSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_stock(request, pk):
    try:
        stock = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    stock.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def get_watchlist(request):
 
    if request.user.is_authenticated:
        user_id = request.user.id
        print("user:", request.user)
        watchlist_symbols = Watchlist.objects.filter(user=user_id).values_list('symbol', flat=True)
        print(watchlist_symbols)
        stock_data = {}
        for symbol in watchlist_symbols:
            stock_data[symbol] = fetch_stock_data(symbol)  # Implement this function to fetch data from Alpha Vantage
        return JsonResponse(stock_data)
    else:
        return JsonResponse({'error': 'User not authenticated'}, status=401)
    
def fetch_stock_data(symbol):
    
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=BK1Y984XVY8NP8SR'#NVTP6VHXJ1OV2UEF'
    response = pip._vendor.requests.get(url)
    data = response.json()
    if 'Time Series (5min)' in data:
        time_series = data['Time Series (5min)']
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        closest_timestamp = min(time_series.keys(), key=lambda x: abs(datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S')))
        return time_series[closest_timestamp]['4. close']
    else:
        print("Error: Time Series (5min) not found in response")
        return None

    symbol = 'AAPL'
    stock_price = fetch_stock_data(symbol)
    if stock_price is not None:
        print(f"The latest stock price for {symbol} is {stock_price}")
    else:
        print("Failed to fetch stock data.")
""" time_series = data.get('Time Series (5min)', {})
    # Get the closest available timestamp to the current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    closest_timestamp = min(time_series.keys(), key=lambda x: abs(datetime.strptime(x, '%Y-%m-%d %H:%M:%S') - datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S')))
    
    latest_data = time_series.get(closest_timestamp, {})
    if not latest_data:
        return None  # or handle the missing data in a way that makes sense

    return latest_data.get('4. close')
"""
    #latest_data = data['Time Series (5min)']['2024-05-16 16:00:00']
    #return latest_data['4. close']
"""
class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
"""
