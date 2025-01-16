# # # test_example.py
# def one_more(x):
#     return x + 1


# def test_correct():
#     assert one_more(4) == 5


# def test_fail():
#     assert one_more(3) == 5
#     # assert one_more(4) == 5

# ########################################################################################

# def get_sort_list(string):
#     new_list = sorted(string.split(', '))
#     return new_list


# def test_sort():
#     """Тестируем функцию get_sort_list()."""
#     result = get_sort_list('Яша, Саша, Маша, Даша')
#     assert result == ['Даша', 'Миша', 'Саша', 'Яша']
#     # assert result == ['Яша', ' Саша', ' Маша', ' Даша']

# ###########################################################################################

# # import pytest

# # def division(dividend, divisor):
# #     return dividend / divisor

# # def test_zero_division():
# #     with pytest.raises(ZeroDivisionError):
# #         division(1, 0)

###############################################################################################

# # test_example.py
# def one_more(x):
#     return x + 1


# def get_sort_list(str):
#     new_list = sorted(str.split(', '))
#     return new_list


# def test_correct():
#     print('Правильный тест')  # Новая строка.
#     assert one_more(4) == 5


# def test_fail():
#     print('Неправильный тест')  # Новая строка.
#     assert one_more(3) == 5


# def test_sort():
#     """Тестируем функцию get_sort_list()."""
#     result = get_sort_list('Яша, Саша, Маша, Даша')
#     assert result == ['Даша', 'Маша', 'Саша', 'Яша']


# def test_type():
#     """Тестируем тип данных, возвращаемых из get_sort_list()."""
#     result = get_sort_list('Яша, Саша, Маша, Даша')
#     # Провальный тест:
#     # ожидаем число, но вернётся список.
#     assert isinstance(result, int)

###############################################################################################

# # test_example.py
# import pytest


# def one_more(x):
#     return x + 1


# def get_sort_list(str):
#     new_list = sorted(str.split(', '))
#     return new_list


# def test_correct():
#     assert one_more(4) == 5


# @pytest.mark.skip(reason='Что-то не работает')  # Маркер.
# def test_fail():
#     assert one_more(3) == 5


# def test_sort():
#     """Тестируем функцию get_sort_list()."""
#     result = get_sort_list('Яша, Саша, Маша, Даша')
#     assert result == ['Даша', 'Маша', 'Саша', 'Яша']


# def test_type():
#     """Тестируем тип данных, возвращаемых из get_sort_list()."""
#     # Провальный тест:
#     # ожидаем число, но вернётся список.
#     result = get_sort_list('Яша, Саша, Маша, Даша')
#     assert isinstance(result, int)

# @pytest.mark.xfail(reason='Пусть пока падает, завтра починю.')
# def test_false():
#     assert False

# @pytest.mark.xfail("sys.version_info < (2, 1)",
#                    reason='Это старая версия Python, чего же вы ждали!')
# def test_for_new_python():
#     # Тест, который провалится на старых версиях Python.
#     assert False

###############################################################################################

# # test_example.py
# import pytest


# def one_more(x):
#     return x + 1


# @pytest.mark.parametrize(
#     'input_arg, expected_result',  # Названия аргументов, передаваемых в тест.
#     [(4, 5), (3, 5)]  # Список кортежей со значениями аргументов.
# )
# # Те же параметры, что и в декораторе.
# def test_one_more(input_arg, expected_result):
#     assert one_more(input_arg) == expected_result

###############################################################################################

# import pytest


# @pytest.fixture  # Декоратор, обозначающий, что эта функция - фикстура.
# def give_me_a_string():
#     return 'Какой чудесный день!'  # Фикстура возвращает строку.


# # Если тестовой функции для работы нужна фикстура, 
# # она указывается в параметрах.
# def test_string_fixture(give_me_a_string):  
#     # Переменная с именем фикстуры содержит в себе объект, 
#     # который вернула фикстура.
#     assert give_me_a_string[0] == 'К'

###############################################################################################

import pytest


@pytest.fixture
def give_me_a_string():
    return 'Какой чудесный день!'


# Новая фикстура возвращает список со строкой из первой фикстуры.
@pytest.fixture
def pack_to_list(give_me_a_string):  # Фикстура может вызывать другие фикстуры.
    return [give_me_a_string]


# Тестовая функция использует обе фикстуры и проверяет их содержимое.
def test_string_fixture(pack_to_list, give_me_a_string):  
    assert pack_to_list != [give_me_a_string]