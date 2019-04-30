from django.shortcuts import render


def index(request):
    return render(request, 'mailmagazine/index.html')


def confirm(request):
    return render(request, 'mailmagazine/confirm.html')
