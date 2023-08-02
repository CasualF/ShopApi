from django.db import models
from category.models import Category
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()


class Product(models.Model):
    STATUS_CHOICES = (
        ('in_stock', 'in_stock'),
        ('out_of_stock', 'out_of_stock')
    )
    stock = models.CharField(choices=STATUS_CHOICES, max_length=20)
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='images', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
