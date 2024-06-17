from django.urls import path
from . import views


app_name = 'product'

urlpatterns = [
    path('', views.ListProductView.as_view(), name='list_product'),
    path('product/detail/<slug:slug>/', views.DetailProductView.as_view(), name='detail_product'),

    path('product/create/<slug:slug>/', views.CreateProductView.as_view(), name='create_product'),
    path('product/update/<slug:slug>/', views.UpdateProductView.as_view(), name='update_product'),
    #path('product/delete/', views.delete_product_view, name='delete_product'),

    path('product_variation/create/<slug:slug>/', views.CreateProductVariationView.as_view(), name='create_variation'),
    path('product_variation/update/<slug:slug>/', views.UpdateProductVariationView.as_view(), name='update_variation'),
    path('product_variation/delete/<slug:slug>/', views.DeleteProductVariationView.as_view(), name='delete_variation'),
]

