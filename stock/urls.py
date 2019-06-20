from django.urls import path

from . import views

urlpatterns = [
    path('get_popularity_data', views.get_popularity_data, name='get_popularity_data'),
    path('get_stock_data', views.get_stock_data, name='get_stock_data'),
    path('get_jetton_data', views.get_jetton_data, name='get_jetton_data'),
]
