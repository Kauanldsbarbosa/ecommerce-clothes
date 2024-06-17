from .forms import StoreCreateForm
from .models import Store
from product import models as product_form
from utils.slugify_and_random_characters import generate_slugify, generate_random_character
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView


class ReadMyStoreView(View):
    template_name = 'store/my_store.html'
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.stores = Store.objects.filter(owner=request.user)
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {'stores': self.stores})

class ReadStoreView(ListView):
    template_name = 'store/read_store.html'
    model = product_form.Product
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.store = Store.objects.filter(slug=self.kwargs['slug']).first()
        context["products"] = product_form.Product.objects.filter(store=self.store)
        context["add_products_enabled"] = self.request.user == self.store.owner
        context["store"] = self.store
        return context
    
    

class CreateStoreView(View):
    template_name = 'store/create_and_update_store.html'
    def get(self, *args, **kwargs):
        form = StoreCreateForm(self.request.POST)
        return render(self.request, self.template_name, {'form': form})
    
    def post(self, *args, **kwargs):
        form = StoreCreateForm(self.request.POST)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.owner = self.request.user
            form_save.slug = generate_slugify(f'{form_save.name}-{generate_random_character()}')
            form.save()
            return redirect('store:read_my_store')
            
        return render(self.request, self.template_name, {'form': StoreCreateForm(self.request.POST)})
    
class UpdateStoreView(View):
    template_name = 'store/create_and_update_store.html'
    def get(self, *args, **kwargs):
        form = StoreCreateForm(self.request.POST or None, instance=Store.objects.filter(slug=self.kwargs['slug']).first())
        return render(self.request, self.template_name, {'form': form})
    
    def post(self, *args, **kwargs):
        form = StoreCreateForm(self.request.POST or None, instance=Store.objects.filter(slug=self.kwargs['slug']).first())
        if form.is_valid():
            form.save()
            return redirect('store:read_my_store')
            
        return render(self.request, self.template_name, {'form': StoreCreateForm(self.request.POST)})
    

class DeleteStoreView(View):
    def get(self, *args, **kwargs):
        store = Store.objects.filter(slug=self.kwargs['slug']).first()
        store.delete()
        return redirect('store:read_my_store')
    