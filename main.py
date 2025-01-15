from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency, transaction_descriptions
from src.transactions import transactions
from src.generators import card_number_generator

print(mask_account_card("Счет 56878990922154165229"))

print(get_date("2024-03-11T02:26:18.671407"))


dictionary: list[dict] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(dictionary, "EXECUTED"))

print(sort_by_date(dictionary, True))

# получаем итератор, отфильтрованный по ключу 'currency'
usd_transactions = filter_by_currency(transactions, "USD")
for i in range(2):
    print(next(usd_transactions))

# получаем описание каждой операции по очереди
descriptions = transaction_descriptions(transactions)
for i in range(5):
    print(next(descriptions))

# генерируем номер карты в диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
for card_number in card_number_generator(1, 5):
    print(card_number)