from product.models import ProductVariation
from django.db import models


class Andress(models.Model):
    name_street = models.CharField(max_length=120, blank=True)
    number = models.CharField(max_length=120, blank=True)
    neighborhood = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=120, blank=True)
    state = models.CharField(max_length=120, blank=True)
    country = models.CharField(max_length=120, blank=True)

    def __str__(self) -> str:
        return self.name_street


class PurchaseOrder(models.Model):
    order_status_choice = (
        ('P', 'Pendente'),
        ('A', 'Aceito'),
        ('S', 'Enviado'),
        ('E', 'Entregue'),
    )
    order_status = models.CharField(max_length=1, choices=order_status_choice, blank=True)
    products = models.ManyToManyField(ProductVariation, blank=True)
    total = models.PositiveIntegerField(blank=True)
    destiny = models.ForeignKey(Andress, on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
