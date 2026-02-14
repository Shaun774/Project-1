from django.urls import path
from .views import create_order,ordersucess

urlpatterns = [
    path("",create_order,   ),
    path('order_sucess/',ordersucess,name="ordersucess")
]