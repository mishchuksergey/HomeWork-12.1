from collections.abc import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict]:
    """
    Функция-генератор возвращает итератор, отфильтрованный по ключу 'currency'
    """
    if not transactions:
        raise Exception("Неверные данные")
    for record in filter(
        lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions
    ):
        yield record


def transaction_descriptions(transactions: list[dict]) -> Generator[str]:
    """Функция-генератор возвращает описание каждой операции по очереди."""
    if transactions == []:
        raise Exception("Неверные данные")
    for descript in map(lambda x: x["description"], transactions):
        yield descript


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """
    Функция-генератор возвращает номер карты в формате ХХХХ ХХХХ ХХХХ ХХХХ,
    где X - цифра номера карты. Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
    """
    if start >= 1 and stop <= 9999999999999999 and start <= stop:
        for number in range(start, stop + 1):
            card_number = str(number).zfill(16)
            yield card_number[:4] + " " + card_number[4:8] + " " + card_number[
                8:12
            ] + " " + card_number[12:16]
    else:
        raise ValueError("Неверные данные")
