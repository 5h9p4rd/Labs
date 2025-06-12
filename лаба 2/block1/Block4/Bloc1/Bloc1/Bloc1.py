import requests
import json
from operator import itemgetter
import os

# Получаем все страны Европы
response = requests.get("https://restcountries.com/v3.region/europe")
countries = response.json()

# Фильтруем страны: не используют евро и площадь > 150000 км²
filtered_countries = []
for country in countries:
    if not isinstance(country, dict):
        continue  # пропускаем элементы, которые не словари
    # Проверка валюты
    currencies = country.get('currencies', {})
    if not currencies:
        continue
    # Валюта может быть словарём или списком, зависит от API, проверим
    # В API v3 обычно currencies — словарь с кодами валют
    if 'EUR' in currencies:
        continue  # пропускаем страны с евро
    
    # Площадь
    area = country.get('area', 0)
    if area <= 150000:
        continue
    
    # Собираем нужные данные
    name = country.get('name', {}).get('common', '')
    capital_list = country.get('capital', [])
    capital = capital_list[0] if capital_list else ''
    population = country.get('population', 0)
    
    # Валюта — берем первую из списка валют
    if isinstance(currencies, dict):
        currency_name = list(currencies.values())[0].get('name') if currencies else ''
    else:
        currency_name = ''
    
    flag_url = country.get('flags', {}).get('png', '')
    
    density = population / area if area else 0
    
    filtered_countries.append({
        'name': name,
        'capital': capital,
        'area': area,
        'population': population,
        'currency': currency_name,
        'flag_url': flag_url,
        'density': density
    })

# Сохраняем в results.json
with open('results.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_countries, f, ensure_ascii=False, indent=4)

# Топ-3 по плотности населения
top3 = sorted(filtered_countries, key=lambda x: x['density'], reverse=True)[:3]
print("Топ-3 стран по плотности населения:")
for country in top3:
    print(f"{country['name']} - {country['density']:.2f} человек/км²")

# Создаем папку для флагов, если не существует
os.makedirs('flags', exist_ok=True)

# Скачиваем флаги для топ-3 стран
import requests

for country in top3:
    flag_url = country['flag_url']
    filename = f"flags/{country['name']}.png"
    try:
        r = requests.get(flag_url)
        with open(filename, 'wb') as f:
            f.write(r.content)
        print(f"Флаг {country['name']} сохранен как {filename}")
    except Exception as e:
        print(f"Не удалось скачать флаг {country['name']}: {e}")
        


