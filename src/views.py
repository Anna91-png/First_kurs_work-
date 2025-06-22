import pandas as pd  # type: ignore
from src.utils import get_greeting, to_json


def main_page(current_time: str) -> str:
    """
    Формирует данные для главной страницы.
    :param current_time: Дата и время в формате 'YYYY-MM-DD HH:MM:SS'
    :return: JSON-строка с приветствием и топ-5 транзакциями
    """
    df = pd.read_csv("data/operations.csv")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    top_transactions = (
        df.sort_values(by="amount", key=abs, ascending=False)
        .head(5)[["date", "amount", "category", "description"]]
        .copy()
    )
    top_transactions["date"] = top_transactions["date"].dt.strftime("%Y-%m-%d")
    result = {
        "greeting": get_greeting(),
        "now": current_time,
        "top_transactions": top_transactions.to_dict(orient="records")
    }
    return to_json(result)
