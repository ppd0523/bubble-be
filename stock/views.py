# -*- coding: utf-8 -*-
from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
from .models import *
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView


class ReportListView(ListAPIView):
    serializer_class = ReportSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        foreign_key = self.kwargs['filter_id']
        date = self.kwargs['date']
        key_q = Filter.objects.get(filter_id=foreign_key)
        queryset = Report.objects.filter(filter_id=key_q, create_date=date)
        return queryset


class FilterListView(ListAPIView):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer


class FilterDetailListView(RetrieveAPIView):
    lookup_field = 'filter_id'
    queryset = Filter.objects.all()
    serializer_class = FilterDetailSerializer


class FilterView(viewsets.ModelViewSet):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer


class ReportView(viewsets.ModelViewSet):
    kq = Filter.objects.get(filter_id='000')
    import datetime as dt
    queryset = Report.objects.filter(filter_id=kq, create_date=dt.datetime.strptime('2021-05-13', '%Y-%m-%d'))
    serializer_class = ReportSerializer


@api_view(['GET', 'POST'])
def report(request, filter_id, date):
    kq = Filter.objects.get(filter_id=filter_id)
    qs = Report.objects.filter(filter_id=kq, create_date=date)
    serializer = ReportSerializer(qs, many=True)
    kwargs = {}
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False}, **kwargs)


@api_view(['GET'])
def price(request, stock_code):
    kwargs = {}
    return JsonResponse({}, safe=False, json_dumps_params={'ensure_ascii': False}, **kwargs)


@api_view(['GET'])
def filter_info(request):
    qs = Filter.objects.all()
    serializer = FilterSerializer(qs, many=True)
    kwargs = {}
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False}, **kwargs)