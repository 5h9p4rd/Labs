import requests
import json
import os

# Получаем данные о европейских странах
response = requests.get('https://restcountries.com/v3.1/region/europe')
countries = response.json()

filtered_countries = []
for country in countries:
    area = country.get('area', 0)
    currencies = country.get('currencies', {})
    uses_euro = 'EUR' in [currency.get('code', '') for currency in currencies.values()]
    
    if area > 150000 and not uses_euro:
        name = country.get('name', {}).get('common', 'Unknown')
        capital = country.get('capital', ['Unknown'])[0]
        population = country.get('population', 0)
        currency_name = list(currencies.keys())[0] if currencies else 'Unknown'
        
        country_data = {
            'name': name,
            'capital': capital,
            'area': area,
            'population': population,
            'currency': currency_name
        }
        filtered_countries.append(country_data)

# Сохраняем данные в файл
with open('results.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_countries, f, ensure_ascii=False, indent=4)

# Вычисляем плотность населения и сортируем
for country in filtered_countries:
    country['density'] = country['population'] / country['area']

sorted_countries = sorted(filtered_countries, key=lambda x: x['density'], reverse=True)
top_3 = sorted_countries[:3]

print("Топ-3 страны по плотности населения:")
for i, country in enumerate(top_3, 1):
    print(f"{i}. {country['name']} - {country['density']:.2f} чел/км²")

# Скачиваем флаги
for country in top_3:
    name = country['name']
    flag_url = f"https://flagcdn.com/w320/{name.lower()}.png"
    flag_response = requests.get(flag_url)
    
    if flag_response.status_code == 200:
        with open(f"{name}_flag.png", 'wb') as f:
            f.write(flag_response.content)
    else:
        print(f"Не удалось загрузить флаг для {name}")
