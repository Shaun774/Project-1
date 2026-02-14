from django.db import models

# Create your models here.
class Order(models.Model):
    product = models.TextField(max_length=100)
    order_date = models.DateField()

    def __str__(self):
        return f"{self.product} date : {self.order_date}"