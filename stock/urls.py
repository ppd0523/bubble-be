from django.urls import path
from . import views

app_name = 'api_stock'
urlpatterns = [
    path('filterInfo/', views.filter_info, name='filter_info'),
    path('report/<str:filter_id>/<str:date>/', views.report, name='filter'),
    path('price/<str:stock_code>/', views.price, name='price'),
]