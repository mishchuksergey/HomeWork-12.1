from unittest.mock import patch
from webbrowser import Error

from src.external_api import convert_current


@patch('requests.get')
def test_convert_current_ok(mock_get):
    """Тест на успешное выполнение конвертации валюты."""
    print(mock_get)
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"info": {"rate": 100}, "result": 100}
    assert convert_current("USD", "RUB", "1") == 100


@patch('requests.get')
def test_convert_current_wrong(mock_get):
    """Тест на провальное выполнение конвертации валюты."""
    print(mock_get)
    mock_get.return_value.status_code != 200
    mock_get.return_value.json.return_value = {"info": {"rate": 100}, "result": 100}
    assert convert_current("USD", "RUB", "1") == Error
