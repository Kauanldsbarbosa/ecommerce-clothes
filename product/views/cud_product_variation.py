from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from product import forms, models


class BaseProductVariation(View):
    def get_slug(self):
        return self.kwargs['slug']
    
    def get_product_by_slug(self, slug):
        product = models.Product.objects.filter(slug=slug).first()
        return product
    
    def get_product_variations_by_product(self, product):
        product_variations = models.ProductVariation.objects.filter(product=product)
        return product_variations
    
    def take_product_of_variation_by_slug(self, slug):
        try:
            _slug = models.ProductVariation.objects.filter(slug=slug).first().product.slug
            product = self.get_product_by_slug(_slug)
            return product
        except:
            return False
    

    def save_variation_form(self, product):
        form_save = self.form.save(commit=False)
        form_save.product = product
        return self.form.save()


class CreateProductVariationView(BaseProductVariation):
    template_name = 'product/variation_create_update.html'
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.form = forms.ProductVariationForm(data=self.request.POST)
        self.product = self.get_product_by_slug(slug=self.get_slug())
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {
            'form': self.form,
            'product': self.product,
            'product_variations': self.get_product_variations_by_product(self.product),
              })
    
    def post(self, *args, **kwargs):
        if self.form.is_valid():
            self.save_variation_form(self.product)
            return redirect('product:create_variation', self.product.slug)
        
        return render(self.request, self.template_name, {'form': self.form,})


class UpdateProductVariationView(BaseProductVariation):
    template_name = 'product/variation_create_update.html'
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.product = self.take_product_of_variation_by_slug(self.get_slug())
        if not self.product:
            self.product = self.get_product_by_slug(self.get_slug())
        self._product_variation = self.get_product_variations_by_product(product=self.product).first()
        self.form = forms.ProductVariationForm(data=self.request.POST or None, instance=self._product_variation)
        self.product_variations = self.get_product_variations_by_product(self.product)
    

    def get(self, *args, **kwargs):
        print(self.product_variations)
        return render(self.request, self.template_name, {
            'form': self.form,
            'product': self.product,
            'product_variations': self.product_variations
              })
    
    def post(self, *args, **kwargs):
        if self.form.is_valid():
            save_form = self.save_variation_form(product=self.product)
            return redirect('product:create_variation', save_form.product.slug)
        
        return render(self.request, self.template_name, {'form': self.form,})
    
class DeleteProductVariationView(BaseProductVariation):
    def get(self, *args, **kwargs):
        product_variation = models.ProductVariation.objects.filter(slug=self.get_slug()).first()
        product_variation.delete()
        print(self.get_product_by_slug(slug=product_variation.product.slug))
        return redirect('product:create_variation', product_variation.product.slug)
