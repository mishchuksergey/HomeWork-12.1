import pytest

from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)
from src.transactions import transactions
from tests.conftest import list_transactions


@pytest.mark.parametrize(
    "transactions_USD",
    [
        (
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
        ),
        (
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            }
        ),
    ],
)
def test_filter_by_currency(list_transactions, transactions_USD):
    """
    Тест функции-генератор отфильтрованной по ключу 'currency' "USD"
    """
    generator = filter_by_currency(list_transactions, "USD")
    next(generator)


def test_filter_by_currency_not_usd(list_transactions_not_usd):
    """
    Тест на ошибку функции-генератор отфильтрованной по ключу 'currency' "USD"
    """
    with pytest.raises(Exception):
        generator = filter_by_currency(list_transactions, "RUB")
        next(generator)


def test_filter_by_currency_empty():
    """
    Тест на ошибку при обработке пустого списка
    """
    with pytest.raises(Exception):
        generator = filter_by_currency(list_transactions_empty, "USD")
        next(generator)


def test_transaction_descriptions(list_transactions):
    """Тест на правильность описания транзакции"""
    for i, description in enumerate(transaction_descriptions(transactions)):
        assert description == list_transactions[i]["description"]


def test_transaction_descriptions_empty(list_transactions_empty):
    """Тест на пустые данные"""
    with pytest.raises(Exception):
        generator = transaction_descriptions(list_transactions_empty)
        next(generator)


@pytest.mark.parametrize(
    "start_number, stop_number, excepted",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9999_9999_9999_9997,
            9999_9999_9999_9999,
            ["9999 9999 9999 9997", "9999 9999 9999 9998", "9999 9999 9999 9999"],
        ),
    ],
)
def test_card_number_generator(start_number, stop_number, excepted):
    "Тест на правильность генерирования номера карты"
    card_number = card_number_generator(start_number, stop_number)

    for i, number in enumerate(card_number):
        assert number == excepted[i]


@pytest.mark.parametrize(
    "start_wrong, stop_wrong",
    [
        (-1, -3),
        (2, -2),
        (-10, -10),
        (9999_9999_9999_9999_9, 5),
        (10, 9999_9999_9999_9999_9),
        (9999_9999_9999_9999_9, 9999_9999_9999_9999_9),
    ],
)
def test_card_number_generator_wrong(start_wrong, stop_wrong):
    "Тест на некорректность диапазона карт"
    with pytest.raises(ValueError):
        cards_wrong = card_number_generator(start_wrong, stop_wrong)
        assert next(cards_wrong)