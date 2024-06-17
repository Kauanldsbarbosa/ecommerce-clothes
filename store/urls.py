from .views import CreateStoreView, ReadMyStoreView, ReadStoreView, UpdateStoreView, DeleteStoreView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'store'

urlpatterns = [
    path('my_store', ReadMyStoreView.as_view(), name='read_my_store'),
    path('create/', CreateStoreView.as_view(), name='create'),
    path('read/<slug:slug>', ReadStoreView.as_view(), name='read_store'),
    path('update/<slug:slug>/', UpdateStoreView.as_view(), name='update'),
    path('delete/<slug:slug>/', DeleteStoreView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
