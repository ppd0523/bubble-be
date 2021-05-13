from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('filter/', views.FilterDetailView.as_view(), name='filter_detail'),
    path('stock/', views.StockDetailView.as_view(), name='stock_detail'),
    path('favorite/', views.FavoriteDetailView.as_view(), name='favorite_detail')
]