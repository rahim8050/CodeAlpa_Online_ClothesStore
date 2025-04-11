from django.db import models
from django.db.models import Sum

from product_app.models import Product


# models.py
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_price(self):
       return sum(item.get_total_price() for item in self.items.all())


# class Cart(models.Model):
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)
#    def get_total_price(self):
#        return sum(item.get_total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="cart_items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def get_total_price(self):
        return self.product.price * self.quantity
