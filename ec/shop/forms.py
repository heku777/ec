from django import forms
from .models import *


class NewProduct(forms.ModelForm):
    class Meta:
        model = ShopItem
        fields = ('name', 'thumbnail', 'price', 'description')
