from django.db import models

# Create your models here.
class Order(models.Model):
    product_name = models.TextField(max_length=100)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} date : {self.order_date}"