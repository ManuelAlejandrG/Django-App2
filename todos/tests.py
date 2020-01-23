from django.test import TestCase

# Create your tests here.
from .models import Todo

class TodoModelTest(TestCase):

	@classmethod
	
	def setUpTestData(cls):
		Todo.objects.create(title="Jugar", description='jugar una vez a la semana')

	def test_title_label(self):
		title = Todo.objects.get(id=1)
		field_label = title._meta.get_field('title').verbose_name
		self.assertEquals(field_label,'title')

	def test_description_label(self):
		title = Todo.objects.get(id=1)
		field_label = title._meta.get_field('description').verbose_name
		self.assertEquals(field_label,'description')

	def test_title_max_length(self):
		title = Todo.objects.get(id=1)
		max_length = todo._meta.get_field('title').max_length
		self.assertEquals(max_length,200)



	
  