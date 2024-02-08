from django.shortcuts import render
from .models import Product, ProductCategory


# Create your views here.
def homepage(request):
    products = Product.objects.all().order_by('price')
    categories = ProductCategory.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)


def menu(request):
    products = Product.objects.all().order_by('price')
    categories = ProductCategory.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'menu.html', context)


def book(request):
    return render(request, 'book.html')


def about(request):
    return render(request, 'about.html')
