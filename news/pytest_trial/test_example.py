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

# test_example.py
def one_more(x):
    return x + 1


def get_sort_list(str):
    new_list = sorted(str.split(', '))
    return new_list


def test_correct():
    print('Правильный тест')  # Новая строка.
    assert one_more(4) == 5


def test_fail():
    print('Неправильный тест')  # Новая строка.
    assert one_more(3) == 5


def test_sort():
    """Тестируем функцию get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result == ['Даша', 'Маша', 'Саша', 'Яша']


def test_type():
    """Тестируем тип данных, возвращаемых из get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    # Провальный тест:
    # ожидаем число, но вернётся список.
    assert isinstance(result, int)
