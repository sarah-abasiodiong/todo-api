from django.test import TestCase
from .models import Register



class RegisterModelTest(TestCase):



    @classmethod
    def setUpTestData(cls):
        Register.objects.create(name='name', email='email')

    def test_title_content(self):
        login = Register.objects.get(id=1)
        expected_object_name = f'{login.name}'
        self.assertEqual(expected_object_name, 'first name')


    def test_body_content(self):
        login = Register.objects.get(id=1)
        expected_object_name = f'{login.email}'
        self.assertEqual(expected_object_name, 'email')