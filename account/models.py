from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAccount(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    date_of_birth = models.DateField(max_length=15, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    account_image = models.ImageField(upload_to='account_image/%Y/%m/%d', null=True, blank=True)
    # andress