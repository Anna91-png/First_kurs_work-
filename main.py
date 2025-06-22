from src.views import main_page
from src.services import cashback_by_category
from src.reports import category_report
import pandas as pd

# Для сервиса - список словарей
data = [
    {"Дата операции": "2024-05-15", "Категория": "Супермаркеты", "Кэшбэк": 100},
    {"Дата операции": "2024-05-18", "Категория": "Фастфуд", "Кэшбэк": 200}
]

if __name__ == "__main__":
    print("--- Главная страница ---")
    print(main_page("2024-05-22 12:00:00"))

    print("--- Выгодные категории кешбэка ---")
    print(cashback_by_category(data, 2024, 5))

    print("--- Траты по категории ---")
    # Для category_report нужен DataFrame
    df = pd.read_csv("data/operations.csv")
    df['date'] = pd.to_datetime(df['date'])
    print(category_report(df, "Супермаркеты", "2024-05-22"))