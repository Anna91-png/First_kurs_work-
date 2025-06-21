import json
import pandas as pd
import datetime as dt


def category_report(df, category, date_str):
    """
    Возвращает сумму трат по категории за последние 3 месяца, включая дату date_str.

    :param df: DataFrame с транзакциями (обязательные столбцы: date, amount, category)
    :param category: Название категории для отчета (строка)
    :param date_str: Дата отсчета (строка в формате 'YYYY-MM-DD')
    :return: JSON-строка с категорией и суммой трат
    """
    date = dt.datetime.strptime(date_str, "%Y-%m-%d")
    start = (date - pd.DateOffset(months=3)).replace(day=1)
    filtered = df[(df['category'] == category) & (df['date'] >= start) & (df['date'] <= date)]
    total = filtered['amount'].sum()
    return json.dumps({"category": category, "total": float(total)}, ensure_ascii=False)