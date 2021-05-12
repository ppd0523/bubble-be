from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('filter/', views.filter_detail, name='filter_detail'),
    path('stock/', views.stock_detail, name='stock_detail'),
    path('favorite/', views.favorite_detail, name='favorite_detail')
]