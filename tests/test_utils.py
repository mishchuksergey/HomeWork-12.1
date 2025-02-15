from unittest.mock import mock_open, patch
from webbrowser import Error

from src.utils import convert_transactions, transaction_amount


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_convert_transactions_valid_file(mock_file):
    """Тест на корректный файл с транзакциями."""
    transactions = convert_transactions("data/operations.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", new_callable=mock_open, read_data='')
def test_convert_transactions_empty_file(mock_file):
    """Тест на пустой файл."""
    transactions = convert_transactions("data/operations.json")
    assert transactions == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_convert_transactions_file_not_found(mock_file):
    """Тест на случай, если файл не найден."""
    transactions = convert_transactions("data/operations.json")
    assert transactions == []


def test_transaction_amount_rub(transaction_rub):
    """Тест на получение суммы в рублях, если транзакция в рублях."""
    assert transaction_amount(transaction_rub) == '31957.58'


@patch("src.utils.convert_current")
def test_transaction_amount_USD_ok(mock_convert_current, transaction_usd):
    """Тест на получение суммы в рублях, если транзакция в иностранной валюте и запрос успешный."""
    mock_convert_current.return_value = 100.00
    result = transaction_amount(transaction_usd)
    assert result == 100.00
    mock_convert_current.assert_called_once_with("USD", "RUB", "1.00")


@patch("src.utils.convert_current")
def test_transaction_amount_USD_wrong(mock_convert_current, transaction_usd):
    """Тест на получение суммы в рублях, если транзакция в иностранной валюте и запрос провальный."""
    mock_convert_current.return_value = Error
    result = transaction_amount(transaction_usd)
    assert result == Error
    mock_convert_current.assert_called_once_with("USD", "RUB", "1.00")
