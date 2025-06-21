import pytest
import pandas as pd
from src.reports import category_report

@pytest.fixture
def sample_df():
    df = pd.DataFrame([
        {"date": "2024-05-15", "amount": -1000, "category": "Супермаркеты"},
        {"date": "2024-05-18", "amount": -800, "category": "Фастфуд"},
        {"date": "2024-05-22", "amount": 5000, "category": "Пополнение"}
    ])
    df['date'] = pd.to_datetime(df['date'])
    return df

@pytest.mark.parametrize("category,expected", [
    ("Супермаркеты", '{"category": "Супермаркеты", "total": -1000.0}'),
    ("Фастфуд", '{"category": "Фастфуд", "total": -800.0}'),
    ("Нет такой", '{"category": "Нет такой", "total": 0.0}')
])
def test_category_report(sample_df, category, expected):
    assert category_report(sample_df, category, "2024-05-22") == expected