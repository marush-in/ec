from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def mypage(request):
    return render(request, 'accounts/mypage.html')


@login_required
def confirmOrderHistory(request):
    return render(request, 'accounts/confirm_order_history.html')


@login_required
def changeDeliveryInfo(request):
    return render(request, 'accounts/change_delivery_info.html')


@login_required
def changeUserInfo(request):
    return render(request, 'accounts/change_user_info.html')


@login_required
def confirmDeleteUser(request):
    return render(request, 'accounts/confirm_delete_user.html')
