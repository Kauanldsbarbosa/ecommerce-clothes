from typing import Iterable
from django.db import models
from account.models import UserAccount
from product.models import ProductVariation
from utils.slugify_and_random_characters import generate_random_character, generate_slugify

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVariation, blank=True, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    selected = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slugify(f'cart item {self.product} {generate_random_character()}')
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return f'{self.product.size} {self.product.color}'

