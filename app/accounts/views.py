from django.shortcuts import render


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')


def mypage(request):
    return render(request, 'accounts/mypage.html')


def confirmOrderHistory(request):
    return render(request, 'accounts/confirm_order_history.html')
