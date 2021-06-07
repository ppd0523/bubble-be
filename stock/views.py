# -*- coding: utf-8 -*-
from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from django.http import JsonResponse


class ReportView(ListCreateAPIView):
    serializer_class = ReportSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        foreign_key = self.kwargs['filter_id']
        date = self.kwargs['date']
        key_q = Filter.objects.get(filter_id=foreign_key)
        queryset = Report.objects.filter(filter_id=key_q, create_date=date)
        return queryset


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
