from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('filter/<str:filter_id>', views.filter_detail, name='filter_detail'),
    path('stock/<str:stock_code>', views.stock_detail, name='stock_detail'),
    path('favorite/<str:favorite_id>', views.favorite_detail, name='favorite_detail')
]