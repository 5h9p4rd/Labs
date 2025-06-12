# Ввод массива целых чисел
numbers = list(map(int, input("Введите массив целых чисел через пробел: ").split()))

# Нахождение максимального элемента и его индекса
max_value = max(numbers)
max_index = numbers.index(max_value)

# Вывод результата
print(f"Максимальный элемент: {max_value}")
print(f"Его порядковый номер (индекс): {max_index+1}")

print("--------------------------------------------")

# Ввод массива целых чисел
numbers = list(map(int, input("Введите массив целых чисел через пробел: ").split()))

# Фильтрация нечетных чисел
odd_numbers = [num for num in numbers if num % 2 != 0]

# Проверка наличия нечетных чисел
if not odd_numbers:
    print("Нечетных чисел в массиве нет.")
else:
    # Сортировка по убыванию
    odd_numbers_sorted = sorted(odd_numbers, reverse=True)
    print("Массив нечетных чисел в порядке убывания:", odd_numbers_sorted)

