"""Декоратор типов"""


def mydecorator(expected_type):
    """
    Декоратор, проверяющий тип параметров функции,
    конвертирующий их по возможности, и складывающий

    Args:
        Аргументы, конвертируемые в ожидаемый тип данных

    Returns:
        Возбуждает исключение ValueError при неудаче конвертации
        Возвращает функцию при успешном исходе конвертации
    """
    def typed(func):
        def wrapper(*args):
            try:
                converted_args = list(map(expected_type, args))
            except (ValueError, TypeError):
                print("Ошибка: Аргумент нельзя сконвертировать в",
                      expected_type.__name__)
                return None
            return func(*converted_args)
        return wrapper
    return typed


@mydecorator(expected_type=str)
def add_str(a, b):
    """
    Функция, выполняющая операцию сложения над аргументами с типом str

    Args:
        Аргументы, прошедшие проверку на ожидаемый тип данных

    Returns:
        Результат операции сложения аргументов
    """
    return a + b


assert add_str(3, "5") == "35", "Ошибка: Результат должен быть '35'"
assert add_str(5, 5) == "55", "Ошибка: Результат должен быть '55'"
assert add_str("a", "b") == "ab", "Ошибка: Результат должен быть 'ab'"


@mydecorator(expected_type=int)
def add_int(a, b, c):
    """
    Функция, выполняющая операцию сложения над аргументами с типом int

    Args:
        Аргументы, прошедшие проверку на ожидаемый тип данных

    Returns:
        Результат операции сложения аргументов
    """
    return a + b + c


assert add_int(5, 6, 7) == 18, "Ошибка: Результат должен быть 18"


@mydecorator(expected_type=float)
def add_float(a, b, c):
    """
    Функция, выполняющая операцию сложения над аргументами с типом float

    Args:
        Аргументы, прошедшие проверку на ожидаемый тип данных

    Returns:
        Результат операции сложения аргументов
    """
    return a + b + c


assert add_float(0.1, 0.2, 0.4) == 0.7000000000000001, \
    "Ошибка: Результат должен быть 0.7000000000000001"
