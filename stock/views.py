# -*- coding: utf-8 -*-
from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ReportListView(ListCreateAPIView):
    serializer_class = ReportSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        foreign_key = self.kwargs['filter_id']
        date = self.kwargs['date']
        key_q = Filter.objects.get(filter_id=foreign_key)
        queryset = Report.objects.filter(filter_id=key_q, create_date=date)
        return queryset


class FilterListView(ListCreateAPIView):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer


class FilterDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer
    print('1', queryset)

    def get_object(self):
        queryset = self.get_queryset()
        filter_id = self.kwargs['filter_id']
        q = queryset.get(filter_id=filter_id)
        # q = get_object_or_404(queryset, filter_id=filter_id)
        return q
