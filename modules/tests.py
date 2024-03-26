from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from modules.models import Module, Lesson
from users.models import User


class ModuleTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@sky.pro")
        self.user.set_password('12345')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_module(self):
        """ тестирование создания модуля """

        response = self.client.post('/users/token/', {
            "email": "admin@sky.pro", "password": "12345"
        })
        self.access_token = response.json().get("access")
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        data_module = {
            'user': self.user.pk,
            'name': 'test',
            'description': 'test',
        }

        response = self.client.post(reverse('modules:module-create'), data=data_module)

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 6, 'name': 'test', 'description': 'test', 'user': 6}
        )

        self.assertTrue(Module.objects.all().exists())

    def test_list_module(self):
        """ тестирование списка модулей """

        self.maxDiff = None

        response = self.client.post('/users/token/', {
            "email": "admin@sky.pro", "password": "12345"
        })
        self.access_token = response.json().get("access")
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        Module.objects.create(
            user=self.user,
            name='list test',
            description='list test',
        )

        response = self.client.get(reverse('modules:module-list'))

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None,
             'results': [{'id': 9, 'name': 'list test', 'description': 'list test', 'user': 9}]}
        )

    def test_detail_module(self):
        """ тестирование информации о модуле """

        response = self.client.post('/users/token/', {
            "email": "admin@sky.pro", "password": "12345"
        })
        self.access_token = response.json().get("access")
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        module = Module.objects.create(

            user=self.user,
            name='test',
            description='test',
        )

        response = self.client.get(
            reverse('modules:module-get', kwargs={'pk': module.pk})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': 8, 'name': 'test', 'description': 'test', 'user': 8})

    def test_update_module(self):
        """ тестирование изменения модуля """

        response = self.client.post('/users/token/', {
            "email": "admin@sky.pro", "password": "12345"
        })
        self.access_token = response.json().get("access")
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        module = Module.objects.create(
            user=self.user,
            name='test',
            description='test',
        )

        data_module_update = {
            'name': 'test1',
        }

        response = self.client.patch(
            reverse('modules:module-update', kwargs={'pk': module.pk}),
            data=data_module_update
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': 10, 'name': 'test1', 'description': 'test', 'user': 11}
        )

    def test_delete_module(self):
        """ тестирование удаления модуля """

        response = self.client.post('/users/token/', {
            "email": "admin@sky.pro", "password": "12345"
        })
        self.access_token = response.json().get("access")
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        module = Module.objects.create(
            user=self.user,
            name='test',
            description='test',
        )

        response = self.client.delete(
            reverse('modules:module-delete', kwargs={'pk': module.pk})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_module_create_validation_error(self):
        """ тест ошибки валидации """

        data = {
            'name': '#@*-^',
            'description': 'test3'
        }

        response = self.client.post(
            reverse('modules:module-create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.module = Module.objects.create(
            name='test12',
            description='test12',
        )

        self.user = User.objects.create(email="admin@sky.pro")
        self.user.set_password('12345')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """ тестирование создания урока """

        response = self.client.post('/users/token/', {
            "email": "admin@sky.pro", "password": "12345"
        })
        self.access_token = response.json().get("access")
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        data_lesson = {
            'module': self.module.pk,
            'user': self.user.pk,
            'name': 'test1',
            'description': 'test1',
        }

        response = self.client.post(reverse('modules:lesson-create'), data=data_lesson)

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'name': 'test1', 'description': 'test1', 'user': 1, 'module': 1}
        )

        self.assertTrue(Lesson.objects.all().exists())

    def test_list_lesson(self):
        """ тестирование списка уроков """

        self.maxDiff = None

        response = self.client.post('/users/token/', {
            "email": "admin@sky.pro", "password": "12345"
        })
        self.access_token = response.json().get("access")
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        Lesson.objects.create(
            module=self.module,
            user=self.user,
            name='list lesson',
            description='list lesson',
        )

        response = self.client.get(reverse('modules:lesson-list'))

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None,
            'results': [{'id': 4, 'name': 'list lesson',
            'description': 'list lesson', 'user': 4, 'module': 4}]}
        )

    def test_detail_lesson(self):
        """ тестирование информации о уроке """

        response = self.client.post('/users/token/', {
            "email": "admin@sky.pro", "password": "12345"
        })
        self.access_token = response.json().get("access")
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        lesson = Lesson.objects.create(
            module=self.module,
            user=self.user,
            name='test',
            description='test',
        )

        response = self.client.get(
            reverse('modules:lesson-get', kwargs={'pk': lesson.pk})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': 3, 'name': 'test', 'description': 'test', 'user': 3, 'module': 3}
        )

    def test_update_lesson(self):
        """ тестирование изменения урока """

        response = self.client.post('/users/token/', {
            "email": "admin@sky.pro", "password": "12345"
        })
        self.access_token = response.json().get("access")
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        lesson = Lesson.objects.create(
            module=self.module,
            user=self.user,
            name='test',
            description='test',
        )

        data_lesson_update = {
            'name': 'test123',
        }

        response = self.client.patch(
            reverse('modules:lesson-update', kwargs={'pk': lesson.pk}),
            data=data_lesson_update
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': 5, 'name': 'test123', 'description': 'test', 'user': 5, 'module': 5}
        )

    def test_delete_lesson(self):
        """ тестирование удаления урока """

        response = self.client.post('/users/token/', {
            "email": "admin@sky.pro", "password": "12345"
        })
        self.access_token = response.json().get("access")
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        lesson = Lesson.objects.create(
            module=self.module,
            user=self.user,
            name='test',
            description='test',
        )

        response = self.client.delete(
            reverse('modules:lesson-delete', kwargs={'pk': lesson.pk})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
