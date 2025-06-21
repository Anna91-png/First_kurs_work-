import json
import datetime as dt


def cashback_by_category(data, year, month):
    """
    Анализирует, сколько можно было заработать кешбэка в разных категориях за указанный месяц года.

    :param data: Список словарей-транзакций с полями "Дата операции", "Категория", "Кэшбэк"
    :param year: Год для анализа
    :param month: Месяц для анализа
    :return: JSON-строка с суммой кешбэка по категориям
    """
    filtered = list(filter(
        lambda tr: (
                dt.datetime.strptime(tr["Дата операции"], "%Y-%m-%d").year == year and
                dt.datetime.strptime(tr["Дата операции"], "%Y-%m-%d").month == month and
                tr.get("Кэшбэк", 0) > 0
        ),
        data
    ))
    result = {}
    for tr in filtered:
        cat = tr["Категория"]
        result[cat] = result.get(cat, 0) + tr["Кэшбэк"]
    return json.dumps(result, ensure_ascii=False)