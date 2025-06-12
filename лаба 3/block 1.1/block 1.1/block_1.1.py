import pickle

# Создание словаря с фильмами и их сборами
movies = {
    "Фильм 1": {"Китай": 100000, "Индия": 200000, "США": 150000, "Россия": 50000, "Франция": 30000, "Германия": 40000},
    "Фильм 2": {"Китай": 200000, "Индия": 150000, "США": 100000, "Россия": 80000, "Франция": 60000, "Германия": 70000},
    "Фильм 3": {"Китай": 50000, "Индия": 100000, "США": 120000, "Россия": 30000, "Франция": 20000, "Германия": 25000},
    "Фильм 4": {"Китай": 300000, "Индия": 250000, "США": 200000, "Россия": 100000, "Франция": 90000, "Германия": 80000},
    "Фильм 5": {"Китай": 150000, "Индия": 180000, "США": 170000, "Россия": 60000, "Франция": 50000, "Германия": 55000},
    "Фильм 6": {"Китай": 80000, "Индия": 90000, "США": 110000, "Россия": 40000, "Франция": 35000, "Германия": 30000},
    "Фильм 7": {"Китай": 250000, "Индия": 220000, "США": 180000, "Россия": 90000, "Франция": 70000, "Германия": 60000},
}

# Вывод списка всех фильмов и их суммарных сборов
total_gross = {movie: sum(gross.values()) for movie, gross in movies.items()}

print("Список всех фильмов и их суммарные сборы:")
for movie, gross in total_gross.items():
    print(f"{movie}: {gross}")

# Вывод фильмов с максимальными и минимальными суммарными сборами
max_gross_movie = max(total_gross, key=total_gross.get)
min_gross_movie = min(total_gross, key=total_gross.get)

print(f"\nФильм с максимальными сборами: {max_gross_movie} ({total_gross[max_gross_movie]})")
print(f"Фильм с минимальными сборами: {min_gross_movie} ({total_gross[min_gross_movie]})")

# Вывод фильмов, превосходящих по суммарным сборам более чем на 25% от минимального по сборам фильма
min_gross = total_gross[min_gross_movie]
threshold = min_gross * 1.25

above_threshold = {movie: gross for movie, gross in total_gross.items() if gross > threshold}

print("\nФильмы, превосходящие по сборам более чем на 25% от минимального:")
for movie, gross in above_threshold.items():
    print(f"{movie}: {gross}")

# Выделение фильмов, сборы которых в Китае меньше их сборов в Индии
china_less_than_india = {movie: gross for movie, gross in movies.items() if gross["Китай"] < gross["Индия"]}

print("\nФильмы, сборы которых в Китае меньше, чем в Индии:")
for movie, gross in china_less_than_india.items():
    print(f"{movie}: {gross}")

# Сохранение словаря в бинарный файл
with open('data.pickle', 'wb') as f:
    pickle.dump(movies, f)

# Чтение словаря из бинарного файла
with open('data.pickle', 'rb') as f:
    loaded_movies = pickle.load(f)

print("\nЗагруженный словарь из файла:")
print(loaded_movies)
