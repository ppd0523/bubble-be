from django.conf import settings
from django.conf.urls import url, static
from . import views

app_name = 'stock2'
urlpatterns = [
    url(r'^conditions/(?P<order>(\d+))$', views.ConditionView.as_view({'get': 'get', 'post': 'create'}), name='condition objects'),
    url(r'^conditions(?:\?order=(\d,)*\d)?', views.ConditionView.as_view({'get': 'get', 'post': 'create'}), name='condition objects'),

]