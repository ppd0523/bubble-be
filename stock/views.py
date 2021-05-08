# -*- coding: utf-8 -*-
from django.http import JsonResponse
from .serializers import FilterEncoder, StockEncoder
from rest_framework.decorators import api_view
from .models import Filter


@api_view(['GET'])
def filter(request, date):
    qs = Filter.objects.filter(create_date=date)
    encoder = FilterEncoder

    kwargs = {}
    response = JsonResponse(qs, encoder, safe=False, json_dumps_params={'ensure_ascii': False}, **kwargs)

    response['Access-Control-Allow-Origin'] = '*'
    return response


@api_view(['GET'])
def price(request, start, end):
    return {'start': start, 'end': end}


@api_view(['GET'])
def condition_name(request, condition_name, date):
    qs = Filter.objects.filter(condition_name=condition_name, create_date=date)
    encoder = FilterEncoder

    kwargs = {}
    response = JsonResponse(qs, encoder, safe=False, json_dumps_params={'ensure_ascii': False}, **kwargs)

    response['Access-Control-Allow-Origin'] = '*'
    return response
