from django.db import models
from account.models import UserAccount


class Store(models.Model):
    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=355, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'
