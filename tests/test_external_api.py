from unittest.mock import patch
from src.external_api import convert_current


@patch('requests.get')
def test_convert_current_ok(mock_get):
    """ Тест на успешное выполнение конвертации валюты. """
    m