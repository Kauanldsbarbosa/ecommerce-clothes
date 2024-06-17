from django.views.generic import ListView, DetailView
from product import models


class ListProductView(ListView):
    model = models.Product
    context_object_name = 'products'
    template_name = 'product/list_products.html'


class DetailProductView(DetailView):
    model = models.Product
    context_object_name = 'product'
    template_name = 'product/detail_product.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["variations"] = models.ProductVariation.objects.filter(product=context["product"])
        context["enable_edit"] = context["product"].store.owner == self.request.user
        return context
    