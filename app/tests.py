from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status


class UserProfileTestCase(APITestCase):
    profile_list_url = reverse('all-profiles')

    def setUp(self):
        # создаем нового пользователя, отправив запрос к конечной точке djoser
        self.user = self.client.post('/auth/users/', data={'username': 'test', 'password': 'some_test'})
        # получаем веб-токен JSON для вновь созданного пользователя
        print('***********', 'setUp', self.user.data['id'])
        response = self.client.post('/auth/jwt/create/', data={'username': 'test', 'password': 'some_test'})
        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    # получаем список всех профилей пользователей во время аутентификации пользователя запроса
    def test_userprofile_list_authenticated(self):
        print('***********', 'test_userprofile_list_authenticated', self.user.data['id'])
        response = self.client.get(self.profile_list_url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # получаем список всех профилей пользователей, пока запрос пользователя не прошел проверку подлинности
    def test_userprofile_list_unauthenticated(self):
        print('***********', 'test_userprofile_list_unauthenticated', self.user.data['id'])
        self.client.force_authenticate(user=None)
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # проверка, чтобы получить данные профиля аутентифицированного пользователя
    def test_userprofile_detail_retrieve(self):
        print('***********', 'test_userprofile_detail_retrieve', self.user.data['id'])
        response = self.client.get(reverse('profile', kwargs={'pk': self.user.data['id']}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # заполнить профиль пользователя, который был автоматически создан с использованием сигналов
    def test_put_userprofile(self):
        profile_data = {'description': 'yes i am'}
        print('***********', 'test_put_userprofile', self.user.data['id'])
        response = self.client.put(reverse('profile', kwargs={'pk': self.user.data['id']}), data=profile_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # закидываем покемон в профиль юзера(аналог test_put_userprofile)
    def test_put_pokemon_to_userprofile(self):
        profile_data = {
            'user': 'test',
            'description': 'bbbbbbbb',
            'pokemon': 1,
        }
        print('***********', 'test_put_pokemon_to_userprofile', self.user.data['id'])
        response = self.client.put(reverse('profile', kwargs={'pk': self.user.data['id']}), data=profile_data)
        print(response)
        print('-------------------------', response.data, '------------------')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # проверка респонса при присваивании покемона профилю
    def test_put_pokemon_to_userprofile_response(self):
        expected_data = {
            'user': 'test',
            'description': 'bbbbbbbb',
            'pokemon': 3,
        }
        profile_data = {
            'user': 'test',
            'description': 'bbbbbbbb',
            'pokemon': 1,
        }
        print('***********', 'test_put_pokemon_to_userprofile_response', self.user.data['id'])
        response = self.client.put(reverse('profile', kwargs={'pk': self.user.data['id']}), data=profile_data)
        print(response.data)
        self.assertEqual(response.data, expected_data)

    # проверка респонса при присваивании покемона профилю
    def test_patch_pokemon_to_userprofile_response(self):
        expected_data = {
            'user': 'test',
            'description': 'something',
            'pokemon': 1,
        }
        profile_data = {
            'description': 'something',
            'pokemon': 1
        }
        print('***********', 'test_patch_pokemon_to_userprofile_response', self.user.data['id'])
        response = self.client.patch(reverse('profile', kwargs={'pk': self.user.data['id']}), data=profile_data)
        print(response.data)
        self.assertEqual(response.data, expected_data)

    # проверка респонса при получении детальной информации профиля
    def test_userprofile_detail_retrieve_response(self):
        expected_data = {
            'user': 'test',
            'description': '',
            'pokemon': None
        }

        print('***********', 'test_userprofile_detail_retrieve_response', self.user.data['id'])
        response = self.client.get(reverse('profile', kwargs={'pk': self.user.data['id']}))
        print(response.data)
        self.assertEqual(response.data, expected_data)

    # проверка респонса при создании профиля
    def test_userprofile_create_response(self):
        expected_data = {
            'email': 'some@gmail.com',
            'username': 'someguy23',
            'id': self.user.data['id'] + 1
        }
        profile_data = {
            'email': 'some@gmail.com',
            'username': 'someguy23',
            'password': '12ghdh1h34h1',
        }
        print('***********', 'test_userprofile_create_response', '******')
        response = self.client.post('/auth/users/', data=profile_data)
        print(response.data)
        self.assertEqual(response.data, expected_data)

    # проверка респонса при удалении профиля
    def test_userprofile_delete_response(self):
        print('***********', 'test_userprofile_create_response', '******')
        response = self.client.delete(reverse('profile', kwargs={'pk': self.user.data['id']}))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
