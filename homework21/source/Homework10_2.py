"""Вернуть число"""


def check_result(func):
    """
    Декоратор, проверяющий,
    является ли результат функции числом

    Args:
        Результат выполнения функцией операции над аргументами

    Returns:
        Возбуждает исключение ValueError
        в случае, если результат функции не является числом
        Возвращает функцию, если результат является числом
    """
    def wrapper(*args):
        try:
            if not isinstance(func(*args), int):
                raise ValueError("Результат не является числом")
        except ValueError as e:
            print(f"Ошибка: {e}")
            return None
        return func(*args)
    return wrapper


@check_result
def arguments(arg1, arg2):
    """
    Функция, выполняющая операции над аргументами
     при условии что результат будет числом

    Args:
        Аргументы, над которыми выполняется операция умножения

    Returns:
        Возращает результат операции, при условии что тот явяется числом
    """
    return arg1 * arg2


assert arguments(2, 3) == 6, "Ошибка: Результат должен быть 6"
assert arguments("2", 3) is None, "Ошибка: Функция должна возвращать None"
assert arguments(5, ["www"]) is None, "Ошибка: Функция должна возвращать None"
