from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from .models import Cart, CartItem
from product.models import ProductVariation
import collections


class AddToCart(View):
    def get(self, *args, **kwargs):
        cart = Cart.objects.filter(user=self.request.user).first()
        product = ProductVariation.objects.filter(slug=self.kwargs['slug']).first()
        repeated_product = self.get_repeat_product(self.get_items_from_cart(cart), product)
        if repeated_product:
            product_with_increased_amount = self.add_more_in_quantity(repeated_product)
            product_with_increased_amount.save()
        else:
            CartItem.objects.create(cart=cart, product=product)
        return redirect(f'{self.request.META.get('HTTP_REFERER')}')
    
    def get_items_from_cart(self, cart):
        cart_items = CartItem.objects.filter(cart=cart)
        return cart_items

    def get_repeat_product(self, items_from_cart, product):
        for item in items_from_cart:
            is_same_size = item.product.size == product.size
            is_same_color = item.product.color == product.color
            if is_same_size and is_same_color:
                return item
    
    def add_more_in_quantity(self, cart_item):
        cart_item.amount += 1
        return cart_item


    
    
class CartView(View):
    template_name = 'cart/cart.html'
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        cart = Cart.objects.filter(user=self.request.user).first()
        self.cart_items = CartItem.objects.filter(cart=cart)

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {'cart_items':self.cart_items})
    

class CartRemoveItemView(View):
    def get(self, *args, **kwargs):
        cart_item = CartItem.objects.filter(slug=self.kwargs['slug']).first()
        cart_item.delete()
        return redirect(f'{self.request.META.get('HTTP_REFERER')}')
