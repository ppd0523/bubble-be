# -*- coding: utf-8 -*-
from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
from .models import *


@api_view(['GET'])
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