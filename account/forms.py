from . import models
from utils.validators import cpf_validation, date_of_birth_validation
from typing import Any
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class UserCreateForm(forms.ModelForm):
    #TODO: adiconar imagefield
    password = forms.CharField(widget=forms.PasswordInput(), label='password')
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), label='password confirmation')
    date_of_birth = forms.DateField(widget=DateInput())
    class Meta:
        model = models.UserAccount
        fields = 'first_name', 'last_name', 'email', 'date_of_birth', 'cpf', 'password', 'password_confirmation'

    def clean(self) -> dict[str, Any]:
        validations_error_messages = {}
        
        if models.UserAccount.objects.filter(email=self.cleaned_data['email']).first():
            validations_error_messages['email'] = 'email has already been registered'

        if cpf_validation.CpfValidation(self.cleaned_data['cpf']).is_valid() == False:
            validations_error_messages['cpf'] = 'Enter a valid CPF'

        if date_of_birth_validation.DateOfBirth.check_if_are_of_legal_age(self.cleaned_data['date_of_birth']) == False:
            validations_error_messages['date_of_birth'] = 'Minors cannot register'

        if len(self.cleaned_data['password']) < 6:
            validations_error_messages['password'] = 'Password must be at least 6 characters long'

        if self.cleaned_data['password'] != self. cleaned_data['password_confirmation']:
            validations_error_messages['password_confirmation'] = "passwords don't match"

        if validations_error_messages:
            raise(forms.ValidationError(validations_error_messages))
    
class UserUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInput())
    class Meta:
        model = models.UserAccount
        fields = 'first_name', 'last_name', 'email', 'date_of_birth', 'cpf'

    def clean(self) -> dict[str, Any]:
        validations_error_messages = {}
        if self.changed_data:
            if cpf_validation.CpfValidation(self.cleaned_data['cpf']).is_valid() == False:
                validations_error_messages['cpf'] = 'Enter a valid CPF'
                return False
            if date_of_birth_validation.DateOfBirth.check_if_are_of_legal_age(self.cleaned_data['date_of_birth']) == False:
                validations_error_messages['date_of_birth'] = 'Minors cannot register'
                return False
                

        if validations_error_messages:
            raise(forms.ValidationError(validations_error_messages))
        
    def check_if_field_has_chaged(self, field):
         self.changed_data

