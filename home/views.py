from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'home/index.html'


class FilterDetailView(TemplateView):
    template_name = 'home/filter_detail.html'


class StockDetailView(TemplateView):
    template_name = 'home/stock_detail.html'


class FavoriteDetailView(TemplateView):
    template_name = 'home/filter_detail.html'