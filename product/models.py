from utils.slugify_and_random_characters import generate_random_character, generate_slugify
from django.db import models
from store.models import Store

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=2080, blank=True)
    price = models.FloatField(default=0.0)
    promotional_price = models.FloatField(default=0.0, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = generate_slugify(f'{self.title}-{generate_random_character()}')
        if not self.title:
            self.title = 'no product name'
        super().save(args, kwargs)
        


class ProductVariation(models.Model):
    sizes_choice = (
        ('p', 'pequeno'),
        ('m', 'medio'),
        ('g', 'grande'),
        ('gg', 'extra grande'),
        ('xg', 'extra extra grande'),
        ('xgg', 'extra extra grande'),
    )
    colors_choice = (
        ('az', 'azul'),
        ('am', 'amarelo'),
        ('bra', 'branco'),
        ('vrd', 'verde'),
        ('vrm', 'vermelho'),
        ('ma', 'marrom'),
        ('ci', 'cinza'),
        ('pr', 'preto'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    size = models.CharField(max_length=3, choices=sizes_choice, blank=True)
    color = models.CharField(max_length=3, choices=colors_choice, blank=True)
    price = models.FloatField(default=0.0)
    promotional_price = models.FloatField(default=0.0, blank=True)
    stock = models.IntegerField(blank=True)
    slug = models.SlugField(unique=True, blank=True)


    def __str__(self) -> str:
        return f'{self.product} {self.size} {self.color}'

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = generate_slugify(f'{self.product} {self.size} {self.color} {generate_random_character()}')
        super().save(args, kwargs)
