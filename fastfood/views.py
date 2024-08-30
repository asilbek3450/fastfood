from django.shortcuts import render, redirect
from .forms import BookTableForm
from .models import Product, ProductCategory, BookTable
from django.core.mail import send_mail
from django.conf import settings


def homepage(request):
    if request.method == 'POST':
        form = BookTableForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # Send email to admin
            subject = 'New Table Booking'
            message = (
                f'Name: {booking.name}\n'
                f'Phone: {booking.phone}\n'
                f'Email: {booking.email}\n'
                f'Date: {booking.date}\n'
                f'Time: {booking.time}\n'
                f'Number of People: {booking.number_of_people}\n'
                f'Message: {booking.message}\n'
            )
            recipient_list = [settings.EMAIL_RECIPIENT_LIST]  # Email to the admin
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

            return redirect('homepage')
        else:
            print('Form is not valid')
    else:
        form = BookTableForm()

    products = Product.objects.all().order_by('price')
    categories = ProductCategory.objects.all()
    context = {
        'form': form,
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)
