from rest_framework import serializers
from . import models


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = '__all__'


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filter
        fields = '__all__'


class FilterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filter
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Price
        fields = '__all__'


class EmptySerializer(serializers.ModelSerializer):
    pass