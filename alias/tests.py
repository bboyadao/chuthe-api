from rest_framework import status
from rest_framework.test import APITestCase
from django.core.management import call_command
from user.models import User
from django.urls import reverse


class UserAliasTests(APITestCase):
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

    def tearDown(self):
        pass

    def test_create_alias(self):
        url = reverse("Alias:user_alias-list")
        data = {'name': 'my alias'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_my_list_aliases(self):
        url_pattern = "Alias:user_alias-list"
        url = reverse(url_pattern)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_update_alias(self):
        url = reverse("Alias:user_alias-detail", kwargs={"pk": 1})
        data = {'name': 'my alias'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_alias(self):
        url = reverse("Alias:user_alias-detail", kwargs={"pk": 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_options_alias(self):
        url = reverse("Alias:user_alias-detail", kwargs={"pk": 1})
        response = self.client.options(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)