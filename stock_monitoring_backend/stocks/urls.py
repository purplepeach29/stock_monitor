from django.urls import path
from . import views

urlpatterns = [
    path('', views.StockList.as_view()),
    path('<int:pk>/', views.StockDetail.as_view()),
    path('login/', views.login),
    path('register/', views.register),
    path('watchlist/', views.get_watchlist),
    path('add/', views.add_stock, name='add_stock'),
    path('delete/<int:pk>/', views.delete_stock, name='delete_stock'),

]
