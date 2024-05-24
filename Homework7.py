"""
Homework_7
"""
# pylint: disable=invalid-name
# Быки и коровы
# Генерируем случайное число с неповторяющимися цифрами
# (Делаем это только один раз в начале)
import random
while True:
    random_number = random.randint(1000, 9999)
    # Проверяем, что все 4 цифры уникальны
    if len(str(random_number)) == len(set(str(random_number))):
        print(random_number)   # Выводим число для отладки (можно убрать)
        break
print("Загадано")

# Начинаем цикл угадывания (загадонное число при этом не меняется)
while True:
    number = int(input("Введите ваше число: "))
    print("Вы ввели:", number)

    cows = 0
    bulls = 0

    # Проверяем на 'коров' (совпадение цифр)
    for i in range(len(str(number))):
        if str(number)[i] in str(random_number):
            cows += 1

    # Проверяем на 'быков' (совпадение цифр и их позиций)
    for i in range(len(str(number))):
        if str(number)[i] == str(random_number)[i]:
            bulls += 1

    print("Коровы:", cows)
    print("Быки:", bulls)

    if bulls == 4:
        print("Вы выиграли!")
        break  # Прерываем цикл, если угадали

# Пирамида
N = 10
for i in range(N):
    print(("*" * (2*i+1)).center(25))

# Статуи
Statues = [6, 2, 3, 8]
Missing_statues = []
for i in range(min(Statues), max(Statues)):
    if i not in Statues:
        Missing_statues.append(i)
print(len(Missing_statues))
