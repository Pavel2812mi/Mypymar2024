"""Модуль для домашнего задания 9."""

# Строки с заданным символом


def delete_symbol(n: str) -> str:
    """
    Функция для удаления символа "#" из строки

    Args:
        n: Начальная строка

    Returns:
        строка без символа "#"
    """
    for i, symbol in enumerate(n):
        if symbol == "#":
            n = n[:i-1] + n[i+1:]
            return delete_symbol(n)
    return n


assert (delete_symbol("a#bc#d")) == "bd"
assert (delete_symbol("abc#d##c")) == "ac"
assert (delete_symbol("abc##d######")) == ""
assert (delete_symbol("#######")) == ""
assert (delete_symbol("")) == ""


# Свечи

def solution(candles_number: int, make_new: int) -> int:
    """
    Функция для расчета общего количества свечей, которые можно сжечь.

    Args:
        candles_number: Начальное количество свечей.
        make_new: Количество остатков, необходимое для создания новой свечи.

    Returns:
        Общее количество свечей, которые можно сжечь.
    """

    total_candles = candles_number
    leftovers = candles_number

    while leftovers >= make_new:
        new_candles = leftovers // make_new
        leftovers = leftovers % make_new + new_candles
        total_candles += new_candles

    return total_candles


assert solution(5, 2) == 9
assert solution(1, 2) == 1
assert solution(15, 5) == 18
assert solution(12, 2) == 23
assert solution(6, 4) == 7
assert solution(13, 5) == 16
assert solution(2, 3) == 2

# Подсчет количества букв


def count_symbol(s):
    """
    Функция сжимает строку,
    заменяя повторяющиеся буквы на букву и количество повторений.

    Args:
        s: Начальная строка.

    Returns:
        Сжатая строка с подсчитанными повторениями букв.
    """

    result = ""
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result += current_char + (str(count) if count > 1 else "")
            current_char = s[i]
            count = 1

    result += current_char + (str(count) if count > 1 else "")

    return result


assert count_symbol("cccbba") == "c3b2a"
assert count_symbol("abeehhhhhccced") == "abe2h5c3ed"
assert count_symbol("aaabbceedd") == "a3b2ce2d2"
assert count_symbol("abcde") == "abcde"
assert count_symbol("aaabbdefffff") == "a3b2def5"
