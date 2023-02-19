from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

indexpage = 'C:\\Farhan\\MyCode\\Python\\My_Own_Learning\\Django_Website\\products\\templates\\index.html'
newproductpage = 'C:\\Farhan\\MyCode\\Python\\My_Own_Learning\\Django_Website\\products\\templates\\newproducts.html'
homepage_page = 'C:\\Farhan\\MyCode\\Python\\My_Own_Learning\\Django_Website\\products\\templates\\homepage.html'
basepage = 'C:\\Farhan\\MyCode\\Python\\My_Own_Learning\\Django_Website\\products\\templates\\base.html'

def index(request):
    products = Product.objects.all()
    return render(request, indexpage, {'products' : products})

def new_product(request):
    return render(request, newproductpage)

def homepage(request):
    return render(request, homepage_page)

def base(request):
    return render(request, basepage)