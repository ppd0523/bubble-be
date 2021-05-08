from django.urls import path
from . import views

app_name = 'api_stock'
urlpatterns = [
    path('filter/<str:filter_id>/<str:date>/', views.filter, name='filter'),
    path('price/<str:stock_code>/', views.price, name='price'),
]