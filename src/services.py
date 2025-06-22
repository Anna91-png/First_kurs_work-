import json
from typing import List, Dict, Any
import datetime as dt

def cashback_by_category(data: List[Dict[str, Any]], year: int, month: int) -> str:
    """
    Возвращает кэшбэк по категориям за месяц в формате JSON.
    """
    now = dt.datetime.now()
    grouped = {}
    for item in data:
        date = str(item["Дата операции"])
        if int(date[:4]) == year and int(date[5:7]) == month:
            cat = str(item["Категория"])
            grouped[cat] = grouped.get(cat, 0) + int(item["Кэшбэк"])
    return json.dumps(grouped, ensure_ascii=False)
