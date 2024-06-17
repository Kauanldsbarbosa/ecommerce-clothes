from django import forms
from .models import Store


class StoreCreateForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = 'name', 'description'
