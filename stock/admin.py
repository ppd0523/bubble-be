from django.contrib import admin
from .models import *


class FilterAdmin(admin.ModelAdmin):
    search_fields = ['filter_id', 'filter_name', 'filter_title']


class ReportAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    search_fields = ['filter_id', 'stock_name', 'create_date']


class PriceAdmin(admin.ModelAdmin):
    # search_fields = ['stock_name']
    date_hierarchy = 'create_date'
    fieldsets = [
        (None, {'fields': ['stock_name']}),
        (None, {'fields': ['create_date']}),
    ]


admin.site.register(Filter, FilterAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Price, PriceAdmin)
