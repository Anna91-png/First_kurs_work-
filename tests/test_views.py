import pytest
import pandas as pd
from src.views import main_page
from unittest.mock import patch
import json

@pytest.fixture
def sample_df():
    df = pd.DataFrame([
        {"date": "2024-05-15", "amount": -1000, "category": "Супермаркеты", "description": "Пятёрочка"},
        {"date": "2024-05-18", "amount": -800, "category": "Фастфуд", "description": "Макдоналдс"},
        {"date": "2024-05-22", "amount": 5000, "category": "Пополнение", "description": "Зарплата"}
    ])
    df['date'] = pd.to_datetime(df['date'])
    return df

def test_main_page_output(sample_df):
    """Проверка структуры ответа и преобразования даты."""
    output = main_page("2024-05-22 12:00:00", sample_df)
    data = json.loads(output)
    assert "greeting" in data
    assert "top_transactions" in data
    assert isinstance(data["top_transactions"], list)
    assert all(isinstance(item["date"], str) for item in data["top_transactions"])

@patch("src.views.get_greeting", return_value="Тестовое приветствие")
def test_main_page_greeting_patch(mock_greet, sample_df):
    output = main_page("2024-05-22 12:00:00", sample_df)
    data = json.loads(output)
    assert data["greeting"] == "Тестовое приветствие"

def test_main_page_empty_df():
    import pandas as pd
    df = pd.DataFrame([], columns=["date", "amount", "category", "description"])
    output = main_page("2024-05-22 12:00:00", df)
    data = json.loads(output)
    assert data["top_transactions"] == []