from django.shortcuts import render


def index(request):
    return render(request, 'products/index.html')


def detail(request):
    return render(request, 'products/product_detail.html')