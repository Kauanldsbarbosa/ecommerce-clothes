from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from account.models import UserAccount

class AccountCreationTest(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.data = {
            'first_name': 'teste',
            'last_name': 'teste',
            'username': 'teste',
            'email': 'teste@teste.com',
            'date_of_birth': datetime(year=1980, month=1, day=1).date(),
            'cpf': '28076498074', 
            'password': 'teste321',
            'password_confirmation': 'test321',
        }

        self.response_get = self.client.get(reverse('account:create'))
        self.response_post = self.client.get(reverse('account:create'), self.data)

        UserAccount.objects.create(email='testeemail@testeemail.com')

    def test_get_method(self):
        self.assertEqual(self.response_get.status_code, 200)


    def test_existing_email_creation(self):
        self.data['email'] = 'testeemail@testeemail.com'
        self.assertEqual(self.response_post.status_code, 200)
    

class LoginTest(TestCase):
    def setUp(self):
        UserAccount.objects.create_user(email='teste@teste.com', password='teste321', username='teste')
        self.data = {
            'email': 'teste@teste.com',
            'password': 'teste321',
            'username': 'teste',
        }
        self.response = self.client.post(reverse('account:login'), self.data)

    def test_redirect_if_user_is_logged_in(self):
        self.assertEqual(self.response.status_code, 302)

    def test_redirected_to_product_list(self):
        self.assertRedirects(self.response, reverse('product:list_product'))

    def test_user_is_logged_in(self):
        self.assertTrue(self.client.login(username=self.data['username'], password=self.data['password']))
