from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mahsulot kategoriyasi'
        verbose_name_plural = 'Mahsulot kategoriyalari'


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.URLField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fast food mahsuloti'
        verbose_name_plural = 'Fast food mahsulotlari'


class BookTable(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    number_of_people = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.date} {self.time} | {self.number_of_people} kishi'

    class Meta:
        verbose_name = 'Stol buyurtma'
        verbose_name_plural = 'Stol buyurtmalar'
