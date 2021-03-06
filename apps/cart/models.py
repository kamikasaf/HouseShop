from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from apps.product.models import Product

# User = get_user_model()


class ShoppingCart(models.Model):

    author = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    date_created = models.DateTimeField(auto_now_add=True)

    def get_total_all_price(self):
        cart_items = self.cart_item.all()
        total = sum([item.get_total_price_item() for item in cart_items])
        return total

    def __str__(self):
        return f'owner:{self.author}'

class CartItem(models.Model):

    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=True, related_name='product_in_cart')
    cart_shopping = models.ForeignKey(to=ShoppingCart, on_delete=models.CASCADE, related_name='cart_item')
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price_item(self):
        return self.product.price * self.quantity


    def __str__(self) -> str:
        return self.cart_shopping.author.email
    
    
    
    
