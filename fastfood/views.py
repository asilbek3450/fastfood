from django.shortcuts import render, redirect

from .forms import BookTableForm
from .models import Product, ProductCategory, BookTable


# Create your views here.
def homepage(request):
    if request.method == 'POST':
        form = BookTableForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('Form is not valid')
    else:
        form = BookTableForm(request.POST)

    products = Product.objects.all().order_by('price')
    categories = ProductCategory.objects.all()
    context = {
        'form': form,
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)
