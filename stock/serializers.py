from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import QuerySet
from .models import Filter


class FilterEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            condition_names = set([o.condition_name for o in obj])
            d = {name: None for name in condition_names}
            for k in d.keys():
                d[k] = {
                    'condition_name': k,
                    'stock_code': [],
                    'stock_name': [],
                }

            for o in obj:
                if o.stock_code and o.stock_name:
                    d[o.condition_name]['stock_code'].append(o.stock_code)
                    d[o.condition_name]['stock_name'].append(o.stock_name)

            data = {
                'data': [v for v in d.values()]
            }

            return data

        elif isinstance(obj, Filter):
            d = {'condition_name': obj.condition_name,
                 'stock_code': [obj.stock_code],
                 'stock_name': [obj.stock_name],
                 }
            return {
                'create_date': obj.create_date.strftime("%Y-%m-%d"),
                'data': [d]
            }

        return super().default(obj)


class StockEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            condition_names = [o.condition_name for o in obj]
            d = {name: None for name in condition_names}
            for k in d.keys():
                d[k] = {
                    'condition_name': k,
                    'stock_code': [],
                    'stock_name': [],
                }

            for o in obj:
                d[o.condition_name]['stock_code'].append(o.stock_code)
                d[o.condition_name]['stock_name'].append(o.stock_name)

            data = {
                'create_date': obj[0].create_date.strftime("%Y-%m-%d"),
                'data': [v for v in d.values()]
            }

            return data

        elif isinstance(obj, Filter):
            d = {'condition_name': obj.condition_name,
                 'stock_code': [obj.stock_code],
                 'stock_name': [obj.stock_name],
                 }
            return {
                'create_date': obj.create_date.strftime("%Y-%m-%d"),
                'data': [d]
            }

        return super().default(obj)