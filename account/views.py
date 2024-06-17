from .import forms
from . import models
from cart.models import Cart
from utils.slugify_and_random_characters import generate_random_character
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View


class CreateAccountView(View):
    template_name = 'account/create_account.html'
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('account:update')
        form = forms.UserCreateForm(data=self.request.POST or None)
        return render(self.request, self.template_name, {'form': form})

    def post(self, *args, **kwargs):
        form = forms.UserCreateForm(self.request.POST or None)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.username = self.set_random_username(f'{self.get_first_name(form)} {self.get_last_name(form)}')
            form_save.set_password(f'{form_save.password}')
            form_save.save()
            Cart.objects.create(user=form_save)
            return redirect('account:login')
        return render(self.request, self.template_name, {'form': form})
    
    def get_first_name(self, form):
        return form.cleaned_data['first_name']
    
    def get_last_name(self, form):
        return form.cleaned_data['last_name']

    def set_random_username(self, text):
        return f'{text}#{generate_random_character(4)}'


class ReadAccount(LoginRequiredMixin, View):
    template_name = 'account/read_account.html'
    login_url = '/login/' 
    def get(self, *args, **kwargs):
        user_account = models.UserAccount.objects.filter(username=self.request.user).first()
        return render(self.request, self.template_name, {'user_account': user_account,})
    def post(self, *args, **kwargs):
        return redirect('account:update')
    

class UpdateAccountView(LoginRequiredMixin, View):
    template_name = 'account/create_account.html'
    login_url = '/login/' 
    def get(self, *args, **kwargs):
        form = forms.UserUpdateForm(self.request.POST or None, instance=self.request.user)
        return render(self.request, self.template_name, {'form': form,})
    
    def post(self, *args, **kwargs):
        form = forms.UserUpdateForm(self.request.POST or None, instance=self.request.user)
        if form.is_valid():
            form.save()
            return redirect('account:read')
        return render(self.request, self.template_name, {'form': form})
    

class DeleteAccount(View):
    def post(self, *args, **kwargs):
        user = models.UserAccount.objects.filter(username=self.request.user).first()
        user.delete()


class LoginAccount(View):
    template_name = 'account/login.html'
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)
    
    def post(self, *args, **kwargs):
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        authenticated_user = authenticate(request=self.request , username=self.get_username_by_email(email), password=password)
        if authenticated_user is not None:
            login(self.request, user=authenticated_user)
            return redirect('product:list_product')
        else:
            messages.error(self.request, 'incorrect email or password.')
            return render(self.request, self.template_name)
    
    def get_username_by_email(self, email):
        try:
            username = models.UserAccount.objects.filter(email=email.lower()).first()
            return username
        except:
            return False

    def get_username_exists_by_email(self, email):
        username = self.get_username_by_email(email)
        if username:
            return True
        else:
            return False


def logout_account(request):
    logout(request)
    return redirect('account:login')
