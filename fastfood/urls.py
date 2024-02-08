from django.urls import path
from .views import homepage, menu, book, about

urlpatterns = [
    path('', homepage, name='homepage'),
    path('menu/', menu, name='menu'),
    path('book/', book, name='book'),
    path('about/', about, name='about'),

]