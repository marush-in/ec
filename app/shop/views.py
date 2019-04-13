from django.shortcuts import render


def index(request):
    return render(request, 'shop/index.html')


def guide(request):
    return render(request, 'shop/guide.html')


def privacy_policy(request):
    return render(request, 'shop/privacy_policy.html')