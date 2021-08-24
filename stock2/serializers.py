from rest_framework import serializers
from . import models


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        exclude = ['id']


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Condition
        fields = ['cond_order', 'cond_name', 'cond_owner', 'create_date']
        write_only_fields = ['file', ]


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Price
        exclude = ['id']
