from django.db.models import Q
from django.shortcuts import render

from products.models import Product


def searchResult(request):
    products = None
    query = None
    count = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(
            Q(name__contains=query) | Q(description__contains=query)
        )
        count = products.count()
    return render(request, 'search/search.html', {
        'query': query,
        'products': products,
        'count': count,
    })
