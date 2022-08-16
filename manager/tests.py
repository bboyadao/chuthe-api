from rest_framework import status
from rest_framework.test import APITestCase
from django.core.management import call_command

from alias.models import Alias
from user.models import User
from django.urls import reverse


class TestPermTests(APITestCase):

    def setUp(self):
        username = "test_user_1"
        password = "test_user_1"
        call_command("mock_alias")
        url = reverse('auth:rest_login')
        body = {
            'username': username,
            'password': password
        }
        response = self.client.post(url, body)
        token = response.data['access_token']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.user = User.objects.get(username=username)

    def test_perm(self):
        url = reverse("Manager:manage_alias-list")
        data = {'name': 'my alias'}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ManageAliasTests(APITestCase):
    def setUp(self):
        username = "admin"
        password = "admin123"
        User.objects.create_superuser(username, 'admin@gmail.com', password)
        call_command("mock_alias")
        url = reverse('auth:rest_login')
        body = {
            'username': username,
            'password': password
        }
        response = self.client.post(url, body)
        token = response.data['access_token']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.user = User.objects.get(username=username)
        assert self.user.is_staff is True

    def test_my_list_aliases(self):
        url_pattern = "Manager:manage_alias-list"
        url = reverse(url_pattern)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'].__len__() > 1, True)
