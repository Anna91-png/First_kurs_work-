from datetime import datetime
from src.utils import cashback_by_category
import json
import pytest

from src.utils import get_greeting, parse_datetime, to_json


@pytest.mark.parametrize(
    "date_str,expected",
    [
        ("2024-01-01 00:00:00", datetime(2024, 1, 1, 0, 0, 0)),
        ("2025-06-21 07:32:35", datetime(2025, 6, 21, 7, 32, 35)),
    ],
)
def test_parse_datetime(date_str, expected):
    assert parse_datetime(date_str) == expected


@pytest.mark.parametrize(
    "hour,expected",
    [
        (1, "Доброй ночи"),
        (9, "Доброе утро"),
        (13, "Добрый день"),
        (21, "Добрый вечер"),
    ],
)
def test_get_greeting(hour, expected):
    date = datetime(2024, 5, 22, hour, 0, 0)
    assert get_greeting(date) == expected


def test_to_json():
    data = {"a": 1, "b": 2}
    result = to_json(data)
    assert isinstance(result, str)
    assert '"a": 1' in result


def test_cashback_by_category_regular():
    data = [
        {"Дата операции": "2024-05-15", "Категория": "Супермаркеты", "Кэшбэк": 100},
        {"Дата операции": "2024-05-18", "Категория": "Фастфуд", "Кэшбэк": 200},
        {"Дата операции": "2024-05-20", "Категория": "Супермаркеты", "Кэшбэк": 50},
        {"Дата операции": "2024-04-18", "Категория": "Фастфуд", "Кэшбэк": 30},
    ]
    result = cashback_by_category(data, 2024, 5)
    assert json.loads(result) == {"Супермаркеты": 150, "Фастфуд": 200}

def test_cashback_by_category_no_matches():
    data = [
        {"Дата операции": "2023-05-15", "Категория": "Супермаркеты", "Кэшбэк": 100},
        {"Дата операции": "2023-05-18", "Категория": "Фастфуд", "Кэшбэк": 200},
    ]
    result = cashback_by_category(data, 2024, 6)
    assert json.loads(result) == {}