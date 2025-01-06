# news/tests/test_trial.py

'''# Запустить все тесты проекта.
python manage.py test

# Запустить только тесты в приложении news.
python manage.py test news

# Запустить только тесты из файла test_trial.py в приложении news.
python manage.py test news.tests.test_trial

# Запустить только тесты из класса Test
# в файле test_trial.py приложения news.  
python manage.py test news.tests.test_trial.Test

# Запустить только тест test_example_fails
# из класса YetAnotherTest в файле test_trial.py приложения news.
python manage.py test news.tests.test_trial.YetAnotherTest.test_example_fails'''

'''это файл для экспериментов с тестами.'''
from django.test import TestCase


class Test(TestCase):

    def test_example_success(self):
        self.assertTrue(True)  # Этот тест всегда будет проходить успешно.


class YetAnotherTest(TestCase):

    def test_example_fails(self):
        self.assertTrue(False)  # Этот тест всегда будет проваливаться.
