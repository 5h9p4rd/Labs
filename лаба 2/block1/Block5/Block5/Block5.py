# Функция для нахождения НОД (алгоритм Евклида)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Функция для деления дробей
def divide_fractions(A, B, C, D):
    # Деление дробей: (A/B) / (C/D) = (A*D) / (B*C)
    numerator = A * D
    denominator = B * C

    # Нахождение НОД для сокращения дроби
    common_divisor = gcd(numerator, denominator)

    # Сокращение дроби
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor

    return simplified_numerator, simplified_denominator

# Ввод данных
A = int(input("Введите числитель первой дроби (A): "))
B = int(input("Введите знаменатель первой дроби (B): "))
C = int(input("Введите числитель второй дроби (C): "))
D = int(input("Введите знаменатель второй дроби (D): "))

# Выполнение деления дробей
result_numerator, result_denominator = divide_fractions(A, B, C, D)

# Вывод результата
print(f"Результат деления дробей: {result_numerator}/{result_denominator}")


# Рекурсивная функция для нахождения суммы n первых членов арифметической прогрессии
def arithmetic_sum(a1, d, n):
    if n == 1:
        return a1  # Базовый случай: сумма одного члена — это сам член
    else:
        # Рекурсивный случай: сумма n членов = текущий член + сумма (n-1) членов
        return a1 + (n - 1) * d + arithmetic_sum(a1, d, n - 1)

# Ввод данных
a1 = int(input("Введите первый член арифметической прогрессии (a1): "))
d = int(input("Введите разность арифметической прогрессии (d): "))
n = int(input("Введите количество членов (n): "))

# Вычисление суммы
sum_result = arithmetic_sum(a1, d, n)

# Вывод результата
print(f"Сумма первых {n} членов арифметической прогрессии: {sum_result}")
