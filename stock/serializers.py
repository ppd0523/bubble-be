from rest_framework import serializers
from . import models


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = ('stock_name', 'stock_code', 'create_date', 'filter_id')


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filter
        fields = ('filter_id', 'filter_title', 'filter_date')


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Price
        fields = ('stock_code', 'stock_name', 'high_price', 'low_price', 'open_price', 'close_price', 'adj_close_price', 'volume', 'create_date')


class RangePriceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DateRange
        fields = ('begin_date', 'end_date')
