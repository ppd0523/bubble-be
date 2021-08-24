from django.contrib import admin
from .models import *


class PriceAdmin(admin.ModelAdmin):
    search_fields = ['stock_name']
    date_hierarchy = 'create_date'
    fieldsets = [
        ('Info', {'fields' : ['stock_code', 'stock_name']}),
        ('Price', {'fields': ['open', 'close', 'high', 'low']}),
        (None, {'fields': ['volume', 'delta']}),
    ]


class ReportAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    search_fields = ['stock_name', 'create_date']


class ConditionAdmin(admin.ModelAdmin):
    search_fields = ['cond_owner']


class ToSubscribeAdmin(admin.ModelAdmin):
    search_fields = ['username', '']


class ToWatchAdmin(admin.ModelAdmin):
    search_fields = ['username']


admin.site.register(Condition, ConditionAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(ToSubscribe, ToSubscribeAdmin)
admin.site.register(ToWatch, ToWatchAdmin)
