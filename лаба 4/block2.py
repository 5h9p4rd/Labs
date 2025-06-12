import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

BASE_URL = "https://worldathletics.org/records/toplists/"
YEARS = range(2001, 2025)
GENDERS = ['men', 'women']
DISCIPLINES = {
    'shot-put': 'Толкание ядра',
    'discus-throw': 'Метание диска',
    'javelin-throw': 'Метание копья',
    'hammer-throw': 'Метание молота'
}

top_results = []

for gender in GENDERS:
    for discipline_code, discipline_name in DISCIPLINES.items():
        for year in YEARS:
            url = urljoin(BASE_URL, f"{discipline_code}/{gender}/senior/{year}")
            response = requests.get(url)
            
            if response.status_code != 200:
                print(f"Ошибка при запросе {url}")
                continue
                
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Находим таблицу с результатами
            table = soup.find('table', {'class': 'records-table'})
            if not table:
                continue
                
            # Первая строка таблицы - топ-1 результат
            row = table.find('tbody').find('tr')
            if not row:
                continue
                
            # Извлекаем данные
            cells = row.find_all('td')
            if len(cells) < 8:
                continue
                
            mark = cells[5].get_text(strip=True)
            name = cells[3].get_text(strip=True)
            country = cells[4].get_text(strip=True)
            date = cells[7].get_text(strip=True)
            
            top_results.append({
                'year': year,
                'gender': 'Мужчины' if gender == 'men' else 'Женщины',
                'discipline': discipline_name,
                'name': name,
                'country': country,
                'mark': mark,
                'date': date
            })

# Сохраняем в CSV
with open('top_results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['year', 'gender', 'discipline', 'name', 'country', 'mark', 'date'])
    writer.writeheader()
    writer.writerows(top_results)

print("Данные успешно сохранены в top_results.csv")
