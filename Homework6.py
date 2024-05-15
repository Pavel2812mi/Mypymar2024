"""
Homework6
"""
# pylint: disable=invalid-name
# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
string = "Robin Singh"
array = string.split()
print(array)

# "I love arrays they are my favorite" =>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]
string1 = "I love arrays they are my favorite"
array1 = string1.split()
print(array1)

# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
array2 = ["Ivan", "Ivanou"]
city = "Minsk"
country = "Belarus"
name = array2[0]
surname = array2[1]
print(f"Привет, {name} {surname}! Добро пожаловать в {city} {country}")

# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
array3 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
string2 = " ".join(array3)
print(string2)

# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "go"]
Numbers.insert(2, 1.5)
print(Numbers)
del Numbers[6]
print(Numbers)
