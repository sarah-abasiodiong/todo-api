from django.test import TestCase
from .models import Task



class TaskModelTest(TestCase):



    @classmethod
    def setUpTestData(cls):
        Task.objects.create(title='first task', body='body')

    def test_title_content(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.title}'
        self.assertEqual(expected_object_name, 'first task')


    def test_body_content(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.body}'
        self.assertEqual(expected_object_name, 'body')