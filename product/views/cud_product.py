from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from product import forms, models
from store import models as store_models
from utils.slugify_and_random_characters import *


class BaseProductView(View):
    def get_slug(self):
        return self.kwargs['slug']
    
    def get_store_by_slug(self, slug):
        return store_models.Store.objects.filter(slug=slug).first()
    
    def save_product_form(self, form, store):
        _save_form = form.save(commit=False)
        _save_form.store = store
        _save_form.slug = generate_slugify(f'{_save_form} {generate_random_character()}')
        return form.save()


class CreateProductView(BaseProductView):
    template_name = 'product/create_update_product.html'
    def setup(self, request, *args, **kwargs) -> None:
        super().setup(request, *args, **kwargs)
        self.form = forms.ProductForm(data=self.request.POST or None)
        self.store = self.get_store_by_slug(slug=self.get_slug())
        self.render = render(self.request, self.template_name, {
            'form': self.form,
              })
    
    def get(self, *args, **kwargs):
        return self.render
    
    def post(self, *args, **kwargs):
        if self.form.is_valid():
            save_form = self.save_product_form(form=self.form, store=self.store)
            return redirect('product:create_variation', save_form.slug)

        return self.render


class UpdateProductView(View):
    template_name = 'product/create_update_product.html'
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.form = self.form = forms.ProductForm(
            data=self.request.POST or None,
            instance=models.Product.objects.filter(slug=kwargs['slug']).first()
            )

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {
            'form': self.form,
              })
    
    def post(self, *args, **kwargs):
        if self.form.is_valid():
            form_save = self.form.save()
            return render(self.request, self.template_name, {
                'form': self.form,
                'slug': form_save.slug,
                })
        return render(self.request, self.template_name, {
                'form': self.form,
                'create_variations': True,
                })

def delete_product_view(request):
    ...