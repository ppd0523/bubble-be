from django.contrib import admin
from .models import *


class FilterAdmin(admin.ModelAdmin):
    search_fields = ['filter_id', 'filter_name', 'filter_title']


class ReportAdmin(admin.ModelAdmin):
    search_fields = ['filter_id', 'stock_code', 'stock_name', 'create_date']


class PriceAdmin(admin.ModelAdmin):
    search_fields = ['stock_code', 'create_date']


admin.site.register(Filter, FilterAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Price, ReportAdmin)
