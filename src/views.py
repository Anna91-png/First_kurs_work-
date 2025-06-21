import pandas as pd
from src.utils import parse_datetime, get_greeting, to_json

def main_page(date_str, df):
    """
    Формирует данные для главной страницы.

    :param date_str: Дата и время в формате 'YYYY-MM-DD HH:MM:SS'
    :param df: DataFrame с транзакциями (обязательные столбцы: date, amount, category, description)
    :return: JSON-строка с приветствием и топ-5 транзакциями
    """
    date = parse_datetime(date_str)
    top_transactions = df.sort_values(by='amount', key=abs, ascending=False).head(5)[["date", "amount", "category", "description"]].copy()
    # Исправление: даже для пустого DataFrame явно приводим тип
    top_transactions['date'] = pd.to_datetime(top_transactions['date'], errors='coerce').dt.strftime('%Y-%m-%d')
    result = {
        "greeting": get_greeting(date),
        "top_transactions": top_transactions.to_dict(orient='records')
    }
    return to_json(result)