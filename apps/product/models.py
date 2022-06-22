from django.db import models
# from django.contrib.auth import get_user_model
from django.conf import settings



class Product(models.Model):
    CATEGORY_CHOICES = (
          ("USA", "USA"),
          ("South Korea", "South Korea"),
          ("Jamaica", "Jamaica"),
          ("Mexico", "Mexico"),
          ("Greece", "Greece"),
          ("Thailand", "Thailand"),
          ("Maldives", "Maldives")
    )

    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    img = models.ImageField(upload_to='products/', blank=True, null=True)
    available = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
            verbose_name='Продукт'
            verbose_name_plural="Продукты"

class ProductImage(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='images', blank=False, null=False)
    image = models.ImageField(upload_to='products/', blank=False, null=False)
    
