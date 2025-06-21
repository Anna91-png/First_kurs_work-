import pytest
from src.services import cashback_by_category
from unittest.mock import patch
from datetime import datetime

@pytest.fixture
def cashback_data():
    return [
        {"Дата операции": "2024-05-15", "Категория": "Супермаркеты", "Кэшбэк": 100},
        {"Дата операции": "2024-05-18", "Категория": "Фастфуд", "Кэшбэк": 200}
    ]

@pytest.mark.parametrize("year,month,expected", [
    (2024, 5, '{"Супермаркеты": 100, "Фастфуд": 200}'),
    (2024, 6, '{}')
])
def test_cashback_by_category(cashback_data, year, month, expected):
    assert cashback_by_category(cashback_data, year, month) == expected

@patch("src.services.dt.datetime")
def test_cashback_by_category_patch_datetime(mock_datetime, cashback_data):
    mock_datetime.strptime.side_effect = lambda s, fmt: datetime(2024, 5, 15)
    result = cashback_by_category(cashback_data, 2024, 5)
    assert '"Супермаркеты"' in result