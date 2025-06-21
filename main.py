import pandas as pd
from src.views import main_page
from src.services import cashback_by_category
from src.reports import category_report

# Пример данных для DataFrame
df = pd.DataFrame([
    {"date": "2024-05-15", "amount": -1000, "category": "Супермаркеты", "description": "Пятёрочка"},
    {"date": "2024-05-18", "amount": -800, "category": "Фастфуд", "description": "Макдоналдс"},
    {"date": "2024-05-22", "amount": 5000, "category": "Пополнение", "description": "Зарплата"}
])
df['date'] = pd.to_datetime(df['date'])

# Для сервиса - список словарей
data = [
    {"Дата операции": "2024-05-15", "Категория": "Супермаркеты", "Кэшбэк": 100},
    {"Дата операции": "2024-05-18", "Категория": "Фастфуд", "Кэшбэк": 200}
]

if __name__ == "__main__":
    print("--- Главная страница ---")
    print(main_page("2024-05-22 12:00:00", df))

    print("--- Выгодные категории кешбэка ---")
    print(cashback_by_category(data, 2024, 5))

    print("--- Траты по категории ---")
    print(category_report(df, "Супермаркеты", "2024-05-22"))