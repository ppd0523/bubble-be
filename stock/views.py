# -*- coding: utf-8 -*-
from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework import permissions
from django.http import HttpResponse, JsonResponse
from sslog.logger import SimpleLogger
import logging
from .viewutils import groupby_data

# logger = SimpleLogger()
# logger.setLevel(logging.INFO)

# Login/Logout
# curl -XPOST http://localhost:52222/auth/login/
# -H'Content-Type: application/json' -d '{
# "username": "asdf", "password": "asdf"}'

# curl -XPOST http://localhost:52222/auth/logout/
# -H'Content-Type: application/json' -d '{
# "username": "asdf"}'


# Create report
# curl -XPOST -H'Content-Type: application/json'
# -H'Authorization: Token ~~~'
# http://localhost:52222/api/filter/<filter_id>/report/<date>/ -d '
# { "stock_codes":["", ""], "stock_names": ["", ""] }'

# Read report
# curl -XGET -H'Content-Type: application/json'
# http://localhost:52222/api/filter/<filter_id>/report/<date>/
class ReportView(ListCreateAPIView):
    serializer_class = ReportSerializer
    model = serializer_class.Meta.model
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        foreign_key = self.kwargs['filter_id']
        date = self.kwargs['date']
        key_q = Filter.objects.get(filter_id=foreign_key)
        queryset = Report.objects.filter(filter_id=key_q, create_date=date)
        return queryset
        # return json.JSONEncoder({'a':10})

    def post(self, request, *args, **kwargs):
        try:
            foreign_key = self.kwargs['filter_id']
            create_date = self.kwargs['date']
            key_q = Filter.objects.get(filter_id=foreign_key)
        except Exception as e:
            return HttpResponse(status=400, content='url error')

        try:
            stock_codes = request.data['stock_codes']
            stock_names = request.data['stock_names']
            if len(stock_codes) != len(stock_names):
                raise Exception('Not matched stock_code and stock_name')
            for stock_code, stock_name in zip(stock_codes, stock_names):
                Report.objects.create(
                    filter_id=key_q,
                    create_date=create_date,
                    stock_code=stock_code,
                    stock_name=stock_name
                )
        except KeyError as e:
            return HttpResponse(status=400, content='key error')
        except Exception as e:
            return HttpResponse(status=400, content=e.message)

        return HttpResponse(status=201, content='create successed')


# Read filter
# curl -XGET -H'Content-Type: application/json'
# http://localhost:52222/api/filter/<filter_id>/

# Create filter
# curl -XPOST -H'Content-Type: application/json'
# -H'Authorization: Token ~~~'
# http://localhost:52222/api/filter/
# { "filter_id": "000", "filter_name": "키움저장이름",
# "filter_title":"잘나가는종목", "create_date": "2021-07-31" }'
class FilterView(ListCreateAPIView):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# curl -XPOST http://localhost:52222/api/filter/
# -H'Authorization: Token ~~~'
# -d '{
#   "filter_id": "000",
#   "filter_name": "키움이름조건식",
#   "filter_title": "상승폭이 가장 빠른 종목들",
#   "filter_date": "2021-07-31"
# }'
class FilterDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        filter_id = self.kwargs['filter_id']
        q = Filter.objects.get(filter_id=filter_id)
        # q = get_object_or_404(queryset, filter_id=filter_id)
        return q


# curl -XPOST http://localhost:52222/stock/000000/price
# -H'Authorization: Token ~~~'
# -d '{
#   stocks: [{
#       'stock_code': "", 'stock_name': "", 'high_price': "", 'low_price': "", 'open_price':"", 'close_price': "",
#       'adj_close': "", 'volume': "", 'date': ""
#   }, {...}, ...]
# }'
class PriceView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        stock_code = self.kwargs['stock_code']
        queryset = Price.objects.filter(stock_code=stock_code).order_by('create_date')
        data = {'stock_code': stock_code, }
        data['days'], data['weeks'], data['months'] = groupby_data(queryset)

        return JsonResponse(data, json_dumps_params={'ensure_ascii': True})

    def post(self, request, *args, **kwargs):
        try:
            stocks = request.data['stocks']
            date = request.data['date']
            for stock in stocks:
                Price.objects.create(
                    stock_code=stock['stock_code'],
                    stock_name=stock['stock_name'],
                    high_price=stock['high_price'],
                    low_price=stock['low_price'],
                    open_price=stock['open_price'],
                    close_price=stock['close_price'],
                    volume=stock['volume'],
                    adj_close_price=stock['close_price'],
                    create_date=stock['date'],
                )
        except KeyError as e:
            return HttpResponse(status=400, content=e)
        except Exception as e:
            return HttpResponse(status=400, content=e)

        return HttpResponse(status=201, content='create successed')


class PriceDateRange(RetrieveUpdateAPIView):
    serializer_class = RangePriceDateSerializer
    model = serializer_class.Meta.model

    def get_object(self):
        stock_code = self.kwargs['stock_code']
        begin, end = None, None
        try:
            queryset = Price.objects.filter(stock_code=stock_code)
            begin = queryset.earliest('create_date').create_date
            end = queryset.latest('create_date').create_date
        except Exception as e:
            pass

        q = DateRange(begin_date=begin, end_date=end)
        return q


