"""Модуль для домашнего задания 10."""

# Положительные аргументы функции


def validate_arguments(func):
    """
    Декоратор, проверяющий,
    все ли аргументы функции являются положительными

    Args:
        Аргументы, проверяемые на положительное числовое значение

    Returns:
         Сообщение об ошибке, если аргументы не являются положительными числами
    """
    def wrapper(*args):
        try:
            for i in args:
                if not isinstance(i, int) or i < 0:
                    func(args)
        except ValueError as e:
            print(f"Ошибка: {e}")
    return wrapper


@validate_arguments
def numbers(*args):
    """
    Функция, передающая аргументы декоратору для проверки
    """
    raise ValueError("Введен неверный аргумент")


numbers(-5)


# Вернуть число

def check_result(func):
    """
    Декоратор, проверяющий,
    является ли результат функции числом

    Args:
        Аргументы, над которыми проводятся операции в функции

    Returns:
        Сообщение об ошибке если результат функции - не число
    """
    def wrapper(arg1, arg2):
        try:
            if not isinstance(func(arg1, arg2), int):
                raise ValueError("Результат не является числом")
        except ValueError as e:
            print(f"Ошибка: {e}")
        return func(arg1, arg2)
    return wrapper


@check_result
def arguments(arg1, arg2):
    """
    Функция, выполняющая операции над аргументами
    при условии что результат будет числом
    """
    return arg1 * arg2


arguments(2, 3)


# Декоратор типов

def mydecorator(expected_type):
    """
    Декоратор, проверяющий тип параметров функции,
    конвертирующий их если надо, и складывающий

    Args:
        Аргументы, проверяемые на корректный тип
        и конвертируемые при необходимости

    Returns:
        Аргументы, прошедшие проверку на тип
        и переданные функции для выполнения операций
    """
    def typed(func):
        def wrapper(*args):
            converted_args = []
            for arg in args:
                if isinstance(arg, list):
                    for item in arg:
                        try:
                            converted_args.append(expected_type(item))
                        except ValueError:
                            print("Ошибка: Результат нельзя сконвертировать")
                            return None
                else:
                    try:
                        converted_args.append(expected_type(arg))
                    except ValueError:
                        print("Ошибка: Результат нельзя сконвертировать")
                        return None
            return func(*converted_args)
        return wrapper
    return typed


@mydecorator(expected_type=str)
def add_str(a, b):
    """
    Функция, выполняющая операцию сложения над аргументами с типом str
    """
    return a + b


print(add_str("go", 123))


@mydecorator(expected_type=int)
def add_int(a, b):
    """
    Функция, выполняющая операцию сложения над аргументами с типом int
    """
    return a + b


print(add_int(1, 3))


@mydecorator(expected_type=float)
def add_float(a, b):
    """
    Функция, выполняющая операцию сложения над аргументами с типом float
    """
    return a + b


print(add_float(1.2, 3.2))


# Функция кэширования *

def cache(func):
    """
    Декоратор для кэширования результатов функции.

    Args:
        func: Функция, результаты которой нужно кэшировать.

    Returns:
        Функция-обертка, которая кэширует результаты func.
    """

    cache_dict = {}  # Словарь для хранения закэшированных значений

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


print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(5))
