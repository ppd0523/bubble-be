from django.urls import path
from . import views

app_name = 'stock'
urlpatterns = [
    path('filter/<str:date>/', views.filter, name='filter'),
    path('filter/<str:condition_name>/<str:date>/', views.condition_name, name='filter'),
    path('price/<str:stock_code>/', views.price, name='price'),
]