"""homework_8"""
# pylint: disable=invalid-name
# Последовательность


def check_increasing_sequence(a):
    """
    Определяет, можно ли получить строго возрастающую последовательность,
    удалив из массива не более одного элемента.
    """
    count = 0
    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            count += 1
            if count > 1:
                return False
        if (i > 0 and a[i - 1] >= a[i + 1]):
            return False
    return True


print(check_increasing_sequence([40, 50, 60, 10, 20, 30]))
print(check_increasing_sequence([1, 3, 2]))
print(check_increasing_sequence([1, 3, 2, 1]))
print(check_increasing_sequence([1, 2, 3, 4, 5, 3, 5, 6]))
print(check_increasing_sequence([1, 2, 3, 1, 4, 1]))

# Число напротив


def find_opposite_number(n, first_number):
    """
    Находит число, которое написано
    в радиально противоположной позиции от first_number.
    """
    if n <= 0 or not isinstance(n, int) or n % 2 != 0:
        return "incorrect circle size"
    if (first_number >= n or first_number < 0
            or not isinstance(first_number, int)):
        return "there is no such number in the circle"
    return (first_number + n // 2) % n


print(find_opposite_number(10, 2))


# Validate
def algorithm_luna(n=None):
    """
    Проверяет, существует ли кредитная карта
    с указанным номером
    """
    if n is None:
        return "Please enter card number"
    if not isinstance(n, int) or n <= 0:
        return "incorrect card number. Try again"

    sum_of_digits = 0
    odd_digits_sum = 0
    even_digits_sum = 0
    for i in range(len(str(n))):
        if int(i) % 2 == 0:
            even_digits_sum += int(str(n)[i]) * 2
            if int(str(n)[i]) * 2 > 9:
                even_digits_sum -= 9
        else:
            odd_digits_sum += int(str(n)[i])
    sum_of_digits = even_digits_sum + odd_digits_sum
    return sum_of_digits % 10 == 0


print(algorithm_luna(4561261212345464))
print(algorithm_luna(4561261212345467))
print(algorithm_luna(5062821234567892))
print(algorithm_luna(5062821734567892))
print(algorithm_luna())
print(algorithm_luna(-5062821734567892))
