from datetime import datetime

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
