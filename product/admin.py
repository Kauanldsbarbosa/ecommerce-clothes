from . import models
from django.contrib import admin


class ProductVariationAdmin(admin.ModelAdmin):
    model = models.ProductVariation


class ProductVariationInline(admin.TabularInline):
    model = models.ProductVariation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    model = models.Product
    inlines = [ProductVariationInline]

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductVariation, ProductVariationAdmin)
