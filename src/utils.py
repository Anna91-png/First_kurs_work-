import datetime as dt
import json


def parse_datetime(date_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> dt.datetime:
    """Преобразует строку в datetime.datetime по формату YYYY-MM-DD HH:MM:SS."""
    return dt.datetime.strptime(date_str, fmt)


def get_greeting() -> str:
    """Возвращает приветствие в зависимости от текущего времени суток."""
    now = dt.datetime.now()
    hour = now.hour
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
