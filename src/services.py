from typing import List, Dict


def cashback_by_category(data: List[Dict[str, int | str]], year: int, month: int) -> str:
    """
    Возвращает категории с максимальным кэшбэком за месяц.
    """
    filtered = [
        item for item in data
        if int(str(item["Дата операции"])[:4]) == year and int(str(item["Дата операции"])[5:7]) == month
    ]
    if not filtered:
        return "Нет операций за этот месяц"
    grouped = {}
    for item in filtered:
        cat = str(item["Категория"])
        grouped[cat] = grouped.get(cat, 0) + int(item["Кэшбэк"])
    max_cashback = max(grouped.values())
    best_cats = [cat for cat, cb in grouped.items() if cb == max_cashback]
    return f"Лучшие категории: {', '.join(best_cats)} (Кэшбэк: {max_cashback})"
