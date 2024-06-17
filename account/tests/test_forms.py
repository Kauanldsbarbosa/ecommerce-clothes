from datetime import datetime
from django.test import TestCase
from account.forms import UserCreateForm
from account.models import UserAccount

class BaseTeste(TestCase):
    def form_data(self):
        data = {
            'first_name': 'teste',
            'last_name': 'teste',
            'email': 'teste@teste.com',
            'date_of_birth': datetime(year=1980, month=1, day=1).date(),
            'cpf': '28076498074',
            'password': 'teste321',
            'password_confirmation': 'teste321',
        }
        return data
    
    def change_form_data_field(self, key, value, data=False):
        if data:
             data[f'{key}'] = value
        else:
            data = self.form_data()
        data[f'{key}'] = value
        return data


class ValidUserCreationTest(BaseTeste):
    def test_valid_user_creation(self):
        form = UserCreateForm(data=self.form_data())
        self.assertTrue(form.is_valid())

class ExistingEmailTest(BaseTeste):
    def setUp(self):
        UserAccount.objects.create(email='duplicate@teste.com')

    def test_existing_email(self):
        data = self.change_form_data_field('email', 'duplicate@teste.com')
        form = UserCreateForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


class InvalidCPFTest(BaseTeste):
    def test_invalid_cpf(self):
        data = self.change_form_data_field('cpf', '11122233344')
        form = UserCreateForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('cpf', form.errors)


class UnderageUserTest(BaseTeste):
    def test_underage_user(self):
        data = self.change_form_data_field('date_of_birth', datetime.now().date())
        form = UserCreateForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('date_of_birth', form.errors)


class PasswordTest(BaseTeste):
    def test_short_password(self):
        _data = self.change_form_data_field('password', 's')
        data = self.change_form_data_field('password_confirmation', 's', _data)

        form = UserCreateForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)

    def test_password_mismatch(self):
        _data = self.change_form_data_field('password', '123456')
        data = self.change_form_data_field('password_confirmation', '654321', _data)

        form = UserCreateForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('password_confirmation', form.errors)

