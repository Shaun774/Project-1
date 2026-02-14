from django.forms import ModelForm
from .models import Order

class Orderform(ModelForm):
    class Meta:
        model = Order
        fields = ["product_name"]