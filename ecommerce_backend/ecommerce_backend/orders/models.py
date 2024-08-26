from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    shipping_address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
