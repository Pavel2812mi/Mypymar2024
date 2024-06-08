"""Функция кэширования"""


def cache(func):
    """
    Декоратор для кэширования результатов функции.

    Args:
        func: Функция, результаты которой нужно кэшировать.

    Returns:
        Функция-обертка, которая кэширует результаты func.
    """

    cache_dict = {}

    def wrapper(*args):
        """
        Обертка, которая проверяет кэш и вызывает функцию при необходимости.

        Args:
            *args: Аргументы функции.

        Returns:
            Результат вызова функции.
        """

        if args not in cache_dict:
            cache_dict[args] = func(*args)
        return cache_dict[args]

    return wrapper


@cache
def fibonacci(n):
    """
    Вычисляет число Фибоначчи для заданного n.

    Args:
        n: Номер числа Фибоначчи.

    Returns:
        Число Фибоначчи.
    """

    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(5) == 5, "Ошибка: Результат должен быть 5"
assert fibonacci(10) == 55, "Ошибка: Результат должен быть 55"
assert fibonacci(5) == 5, "Ошибка: Результат должен быть 5"
