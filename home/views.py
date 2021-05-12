from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def filter_detail(request):
    return render(request, 'home/filter_detail.html')


def stock_detail(request):
    return render(request, 'home/stock_detail.html')


def favorite_detail(request):
    return render(request, 'home/filter_detail.html')