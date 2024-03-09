from django.shortcuts import render


def home(request):
    return render(request, 'mart_app/home.html')


def product_detail(request):
    return render(request, 'mart_app/productdetail.html')


def add_to_cart(request):
    return render(request, 'mart_app/addtocart.html')


def buy_now(request):
    return render(request, 'mart_app/buynow.html')


def profile(request):
    return render(request, 'mart_app/profile.html')


def address(request):
    return render(request, 'mart_app/address.html')


def orders(request):
    return render(request, 'mart_app/orders.html')


def change_password(request):
    return render(request, 'mart_app/changepassword.html')


def mobile(request):
    return render(request, 'mart_app/mobile.html')


def login(request):
    return render(request, 'mart_app/login.html')


def customer_registration(request):
    return render(request, 'mart_app/customerregistration.html')


def checkout(request):
    return render(request, 'mart_app/checkout.html')
