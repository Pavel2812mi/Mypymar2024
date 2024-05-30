"""Модуль для домашнего задания 7."""

# pylint: disable=invalid-name
# Быки и коровы
import random
while True:
    random_number = random.randint(1000, 9999)
    if len(str(random_number)) == len(set(str(random_number))):
        print(random_number)
        break
print("Загадано")

while True:
    number = input("Введите ваше число: ")
    print("Вы ввели:", number)

    if len(set(number)) != len(number):
        print("Число должно содержать только уникальные цифры.")
        continue

    cows = 0
    bulls = 0

    for i in range(len(str(number))):
        for j in range(len(str(random_number))):
            if i != j and str(number)[i] == str(random_number)[j]:
                cows += 1

    for i in range(len(str(number))):
        for j in range(len(str(random_number))):
            if i == j and str(number)[i] == str(random_number)[j]:
                bulls += 1

    print("Коровы:", cows)
    print("Быки:", bulls)

    if bulls == 4:
        print("Вы выиграли!")
        break

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
