from django.test import TestCase
from udms.models import DisciplinaryCase

class DisciplinaryCaseTestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        DisciplinaryCase.objects.create(title='cheating exams', description='was caught cheating in final exams')
    
    def test_title_label(self):
        case = DisciplinaryCase.objects.get(id=1)
        field_label = case._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        case = DisciplinaryCase.objects.get(id=1)
        field_label = case._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')