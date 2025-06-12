# Ввод строки с клавиатуры
input_string = input("Введите строку: ")

# Замена буквы 'а' на 'о' и подсчет количества замен
modified_string = input_string.replace('а', 'о').replace('А', 'О')
replace_count = input_string.count('А') + input_string.count('а')

# Подсчет общего количества символов в строке
total_characters = len(input_string)

# Вывод результатов
print(f"Модифицированная строка: {modified_string}")
print(f"Количество замен 'а' на 'о': {replace_count}")
print(f"Общее количество символов в строке: {total_characters}")
