def convert_to_kilograms(unit, mass):
    if unit == 1:
        return mass  # Уже в килограммах
    elif unit == 2:
        return mass / 1_000_000  # Миллиграммы в килограммы
    elif unit == 3:
        return mass / 1000  # Граммы в килограммы
    elif unit == 4:
        return mass * 1000  # Тонны в килограммы
    elif unit == 5:
        return mass * 100  # Центнеры в килограммы
    else:
        return None  # Некорректный номер единицы измерения

def main():
    # Выводим доступные единицы измерения
    print("Выберите единицу измерения:")
    print("1 — килограмм")
    print("2 — миллиграмм")
    print("3 — грамм")
    print("4 — тонна")
    print("5 — центнер")

    import sys
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Ввод номера единицы измерения
    unit = int(input("Введите номер единицы измерения (1-5): "))
    
    # Ввод массы
    mass = float(input("Введите массу: "))

    # Преобразование массы в килограммы
    result = convert_to_kilograms(unit, mass)

    if result is not None:
        print(f"Масса в килограммах: {result} кг")
    else:
        print("Ошибка: введен некорректный номер единицы измерения.")

if __name__ == "__main__":
    main()