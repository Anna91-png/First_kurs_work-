import pandas as pd  # type: ignore
import datetime as dt
import json
import os
from functools import wraps


def report_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("=== Отчет ===")
        result = func(*args, **kwargs)
        print("=============")
        return result
    return wrapper


def save_report_decorator(func):
    """Декоратор для сохранения результата работы отчета в файл."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Имя файла: имя_функции_YYYYMMDD_HHMMSS.json
        timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        func_name = func.__name__
        filename = f"{func_name}_{timestamp}.json"
        dirpath = "saved_reports"
        os.makedirs(dirpath, exist_ok=True)
        filepath = os.path.join(dirpath, filename)
        # Если результат строка, но содержит JSON — сохраняем красиво
        try:
            json_obj = json.loads(result)
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(json_obj, f, ensure_ascii=False, indent=2)
        except Exception:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(str(result))
        print(f"Отчет сохранён: {filepath}")
        return result
    return wrapper


@save_report_decorator
@report_decorator
def category_report(df: pd.DataFrame, category: str, date_str: str) -> str:
    """
    Возвращает сумму трат по категории за последние 3 месяца, включая дату date_str.
    """
    date = dt.datetime.strptime(date_str, "%Y-%m-%d")
    start = (date - pd.DateOffset(months=3)).replace(day=1)
    filtered = df[(df["category"] == category) & (df["date"] >= start) & (df["date"] <= date)]
    total = filtered["amount"].sum()
    return json.dumps({"category": category, "total": float(total)}, ensure_ascii=False)


@save_report_decorator
@report_decorator
def total_report(df: pd.DataFrame, date_str: str) -> str:
    """
    Возвращает общую сумму трат за последние 3 месяца, включая дату date_str.
    """
    date = dt.datetime.strptime(date_str, "%Y-%m-%d")
    start = (date - pd.DateOffset(months=3)).replace(day=1)
    filtered = df[(df["date"] >= start) & (df["date"] <= date)]
    total = filtered["amount"].sum()
    return json.dumps({"total": float(total)}, ensure_ascii=False)