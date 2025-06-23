import datetime as dt
import json
from typing import List, Dict, Any

def parse_datetime(date_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> dt.datetime:
    """Преобразует строку в datetime.datetime по формату YYYY-MM-DD HH:MM:SS."""
    return dt.datetime.strptime(date_str, fmt)

def get_greeting(date: dt.datetime = None) -> str:
    """Возвращает приветствие в зависимости от времени суток."""
    if date is None:
        date = dt.datetime.now()
    hour = date.hour
    if 0 <= hour <= 5:
        return "Доброй ночи"
    elif 6 <= hour <= 11:
        return "Доброе утро"
    elif 12 <= hour <= 17:
        return "Добрый день"
    else:
        return "Добрый вечер"

def to_json(data: object) -> str:
    """Возвращает объект в виде красиво отформатированной JSON-строки."""
    return json.dumps(data, ensure_ascii=False, indent=2)

def cashback_by_category(data: List[Dict[str, Any]], year: int, month: int) -> str:
    """
    Возвращает кэшбэк по категориям за месяц в формате JSON.
    """
    grouped = {}
    for item in data:
        date = str(item["Дата операции"])
        if int(date[:4]) == year and int(date[5:7]) == month:
            cat = str(item["Категория"])
            grouped[cat] = grouped.get(cat, 0) + int(item["Кэшбэк"])
    return json.dumps(grouped, ensure_ascii=False)
