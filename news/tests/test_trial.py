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

# news/tests/test_trial.py
# from django.test import TestCase

# from news.models import News


# class TestNews(TestCase):
#     # Все нужные переменные сохраняем в атрибуты класса.
#     TITLE = 'Заголовок новости'
#     TEXT = 'Тестовый текст'
    
#     @classmethod
#     def setUpTestData(cls):
#         cls.news = News.objects.create(
#             # При создании объекта обращаемся к константам класса через cls.
#             title=cls.TITLE,
#             text=cls.TEXT,
#         )

#     def test_successful_creation(self):
#         news_count = News.objects.count()
#         self.assertEqual(news_count, 1)

#     def test_title(self):
#         # Чтобы проверить равенство с константой -
#         # обращаемся к ней через self, а не через cls:
#         self.assertEqual(self.news.title, self.TITLE)