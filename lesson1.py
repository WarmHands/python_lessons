# Урок первый 1.2
# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


def seconds_to_time(seconds):
    seconds = int(seconds)
    ss = seconds % 60
    mm = (seconds // 60) % 60
    hh = seconds // 3600
    return "%02d:%02d:%02d" % (hh, mm, ss)


# input_seconds = input("Введите кол-во секунд: ")
print(seconds_to_time(3685))


# Урок первый 1.3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369
def triplet_sum_number(number):
    n1 = number
    n2 = n1 * 10 + n1
    n3 = n2 * 10 + n1
    return n1 + n2 + n3  # Отвратительная реализация


print(triplet_sum_number(3))


# Урок первый 1.4
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции


def max_digit(task_number):
    max_number = -1
    while task_number > 10:
        number_to_check = task_number % 10
        task_number //= 10
        if number_to_check > max_number:
            max_number = number_to_check
    return max_number


print(max_digit(123456789))