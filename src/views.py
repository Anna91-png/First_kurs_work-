import pandas as pd  # type: ignore
from src.utils import get_greeting, to_json

def main_page(date_str: str, df: pd.DataFrame) -> str:
    """
    Формирует данные для главной страницы.

    :param date_str: Дата и время в формате 'YYYY-MM-DD HH:MM:SS'
    :param df: DataFrame с данными по операциям
    :return: JSON-строка с приветствием, сводной информацией и топ-5 транзакциями
    """
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Топ-5 транзакций по модулю суммы
    top_transactions = (
        df.sort_values(by="amount", key=abs, ascending=False)
        .head(5)[["date", "amount", "category", "description"]]
        .copy()
    )
    top_transactions["date"] = top_transactions["date"].dt.strftime("%Y-%m-%d")

    # Суммарные показатели
    total_count = len(df)
    total_expenses = df[df["amount"] < 0]["amount"].sum()
    total_income = df[df["amount"] > 0]["amount"].sum()
    balance = df["amount"].sum()
    categories = sorted(df["category"].unique())

    result = {
        "greeting": get_greeting(),
        "now": date_str,
        "total_operations": total_count,
        "total_expenses": float(total_expenses),
        "total_income": float(total_income),
        "balance": float(balance),
        "categories": categories,
        "top_transactions": top_transactions.to_dict(orient="records")
    }
    return to_json(result)