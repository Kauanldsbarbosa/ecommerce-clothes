from . import models
from django.contrib import admin


class PurchaseOrderAdmin(admin.ModelAdmin):
    model = models.PurchaseOrder

admin.site.register(models.PurchaseOrder, PurchaseOrderAdmin)
