from django.conf.urls import url
from . import views


app_name = 'api_stock'
urlpatterns = [
    url(r'filter/(?P<filter_id>\w{3})/report/(?P<date>\d{4}-\d{2}-\d{2})', views.ReportListView.as_view()),
    url(r'filter/(?P<filter_id>\w{3})/', views.FilterDetailListView.as_view()),
    url('filter/', views.FilterListView.as_view()),
    # path('filterInfo/', views.filter_info, name='filter_info'),
    # path('report/<str:filter_id>/<str:date>/', views.report, name='filter'),
    # path('price/<str:stock_code>/', views.price, name='price'),
]