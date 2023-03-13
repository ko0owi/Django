from django import forms
from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('name','car','phone', 'start_rent','stop_rent')