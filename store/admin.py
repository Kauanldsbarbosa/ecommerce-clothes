from django.contrib import admin
from .models import Store

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    fields = 'owner', 'name', 'description', 'slug'

admin.site.register(Store, StoreAdmin)