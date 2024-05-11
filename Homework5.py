"""
Homework5
"""
# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
# pylint: disable=invalid-name
website = 'www.my_site.com#about'
new_website = website.replace("#", "/")
print(new_website)

# Напишите программу, которая добавляет ‘ing’ к словам


def add_ing(word):
    """
    Добавляет суффикс 'ing' к заданному слову.

    Args:
        input_word: Слово, к которому нужно добавить 'ing'.

    Returns:
        output_word: Измененное слово с добавленным 'ing'.
    """
    word = word+"ing"
    return word


# Пример использования
input_word = "Hello"
output_word = add_ing(input_word)
print(output_word)

# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
name = "Ivanou Ivan"
new_name = name[7:11] + " " + name[0:6]
print(new_name)

# Имена собственные всегда начинаются с заглавной буквы,
# за которой следуют строчные буквы.
# Исправьте данное имя собственное так,
# чтобы оно соответствовало этому утверждению.
# "pARiS" >> "Paris"

city = "pARiS"
print(city.title())

# Напишите программу которая удаляет пробел в начале, в конце строки:


def remove_spaces_start(text):
    """
    Удаляет пробелы в начале строки:

    Args:
        input_text: Текст, из которого нужно убрать пробел.

    Returns:
        output_text: Измененный текст с удаленным пробелом.
    """
    text = text.lstrip()
    return text


# Пример использования
input_text = "   Hi. how are you?"
output_text = remove_spaces_start(input_text)
print(output_text)


def remove_spaces_end(text):
    """
    Удаляет пробелы в конце строки:

    Args:
        input_text2: Текст, из которого нужно убрать пробел.

    Returns:
        output_text2: Измененный текст с удаленным пробелом.
    """
    text = text.rstrip()
    return text


# Пример использования
input_text2 = "Hi. how are you?    "
output_text2 = remove_spaces_end(input_text2)
print(output_text2)
