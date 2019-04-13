from django.shortcuts import render


def index(request):
    return render(request, 'shop/index.html')


def guide(request):
    return render(request, 'shop/guide.html')


def privacy_policy(request):
    return render(request, 'shop/privacy_policy.html')


def company(request):
    return render(request, 'shop/company.html')


def terms_of_use(request):
    return render(request, 'shop/terms_of_use.html')


def faq(request):
    return render(request, 'shop/faq.html')


def legal(request):
    return render(request, 'shop/legal.html')
