import os
import shutil

def show_file_content():
    file_name = input("Введите имя файла: ")
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            print(file.read())
    else:
        print("Файл не найден!")

def find_files():
    search_term = input("Введите имя или часть имени файла: ")
    found_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if search_term in file:
                found_files.append(os.path.join(root, file))
    if found_files:
        print("Найденные файлы:")
        for file in found_files:
            print(file)
    else:
        print("Файлы не найдены.")

def list_directory():
    dir_path = input("Введите путь к директории: ")
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        print(f"Содержимое директории {dir_path}:")
        for item in os.listdir(dir_path):
            print(item)
    else:
        print("Директория не найдена!")

def create_file_or_folder():
    path = input("Введите путь и имя файла/папки: ")
    if not path:
        print("Неверный путь!")
        return
    if os.path.exists(path):
        print("Файл или папка уже существуют!")
        return
    if input("Создать файл (1) или папку (2)? ") == "1":
        with open(path, 'w', encoding='utf-8') as file:
            print(f"Файл {path} создан.")
    else:
        os.makedirs(path)
        print(f"Папка {path} создана.")

def main():
    while True:
        print("\n--- Файловый менеджер ---")
        print("1. Показать содержимое файла")
        print("2. Найти файл/файлы")
        print("3. Раскрыть директорию")
        print("4. Создать файл/папку")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            show_file_content()
        elif choice == "2":
            find_files()
        elif choice == "3":
            list_directory()
        elif choice == "4":
            create_file_or_folder()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
