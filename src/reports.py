import pandas as pd  # type: ignore
import datetime as dt
import json
from functools import wraps


def report_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("=== Отчет ===")
        result = func(*args, **kwargs)
        print("=============")
        return result
    return wrapper


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