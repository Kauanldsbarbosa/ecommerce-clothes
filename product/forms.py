from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from . import models
from store.models import Store
from account.models import UserAccount

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = 'title', 'description', 'price', 'promotional_price'
    
        

class ProductVariationForm(forms.ModelForm):
    class Meta:
        model = models.ProductVariation
        fields = 'size', 'color', 'stock', 'price', 'promotional_price',
