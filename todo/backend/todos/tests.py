from django.test import TestCase

# Create your tests here.
from .models import Todo

class TodoModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Todo.objects.create(title='Test Todo', description='This is a test todo item.', completed=False)
        
    def test_title_label(self):
        todo = Todo.objects.get(id=1)
        field_label = todo._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
    
    def test_description_label(self):
        todo = Todo.objects.get(id=1)
        field_label = todo._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')