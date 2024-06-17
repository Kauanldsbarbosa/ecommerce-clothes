from . import views
from django.urls import path


app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='read_cart'),
    path('add_to_cart/<slug:slug>', views.AddToCart.as_view(), name='add_to_cart'),
    path('remove_to_cart/<slug:slug>', views.CartRemoveItemView.as_view(), name='remove_to_cart'),
    ]