from django.contrib import admin
from . import models


class UserAccountAdmin(admin.ModelAdmin):
    model = models.UserAccount

admin.site.register(models.UserAccount, UserAccountAdmin)