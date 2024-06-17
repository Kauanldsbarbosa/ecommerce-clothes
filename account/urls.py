from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('create/', views.CreateAccountView.as_view(), name='create'),
    path('read/', views.ReadAccount.as_view(), name='read'),
    path('update/', views.UpdateAccountView.as_view(), name='update'),
    path('login/', views.LoginAccount.as_view(), name='login'),
    path('logout/', views.logout_account, name='logout'),
]