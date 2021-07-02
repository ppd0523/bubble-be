# -*- coding: utf-8 -*-
from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework import permissions
from django.http import HttpResponse
from sslog.logger import SimpleLogger
import logging
logger = SimpleLogger()
logger.setLevel(logging.INFO)


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

    def post(self, request, *args, **kwargs):
        try:
            foreign_key = self.kwargs['filter_id']
            create_date = self.kwargs['date']
            key_q = Filter.objects.get(filter_id=foreign_key)
        except Exception as e:
            return HttpResponse(status=400, content='url error')

        print(request.data)
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


class FilterView(ListCreateAPIView):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer


class FilterDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer

    def get_object(self):
        filter_id = self.kwargs['filter_id']
        q = Filter.objects.get(filter_id=filter_id)
        # q = get_object_or_404(queryset, filter_id=filter_id)
        return q


class PriceView(ListCreateAPIView):
    serializer_class = PriceSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        stock_code = self.kwargs['stock_code']
        queryset = Price.objects.filter(stock_code=stock_code).order_by('create_date')
        return queryset


class PriceDateRange(RetrieveUpdateAPIView):
    serializer_class = RangePriceDateSerializer
    model = serializer_class.Meta.model

    def get_object(self):
        stock_code = self.kwargs['stock_code']
        queryset = Price.objects.filter(stock_code=stock_code)
        begin = queryset.earliest('create_date').create_date
        end = queryset.latest('create_date').create_date
        q = DateRange(begin_date=begin, end_date=end)
        return q
