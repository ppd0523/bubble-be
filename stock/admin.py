from django.contrib import admin
from .models import Filter


class FilterAdmin(admin.ModelAdmin):
    search_fields = ['condition_name', 'create_date', 'stock_code', 'stock_name']


admin.site.register(Filter, FilterAdmin)