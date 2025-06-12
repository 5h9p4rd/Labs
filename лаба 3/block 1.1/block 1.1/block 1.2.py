
# Открываем файл input.txt для чтения
with open('input.txt', 'r', encoding='utf-8') as input_file:
    # Читаем все строки из файла
    lines = input_file.readlines()

# Переводим все слова в каждой строке в верхний регистр
uppercased_lines = [line.upper() for line in lines]

# Открываем файл output.txt для записи
with open('output.txt', 'w', encoding='utf-8') as output_file:
    # Записываем строки в верхнем регистре в output.txt
    output_file.writelines(uppercased_lines)

print("Результат успешно записан в файл output.txt")