from django.conf.urls import url
from . import views


app_name = 'api_stock'
urlpatterns = [
    url(r'filter/(?P<filter_id>\d{3})/report/(?P<date>\d{4}-\d{2}-\d{2})/$', views.ReportView.as_view()),
    url(r'filter/(?P<filter_id>\d{3})/$', views.FilterDetailView.as_view()),
    url(r'filter/$', views.FilterView.as_view()),
]