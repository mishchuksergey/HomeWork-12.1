def filter_by_state(dictionary: list[dict], state: str) -> list[dict] | None:
    """Функция,которая возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    new_dictionary: list[dict] = [{}]
    for date in dictionary:
        if date["state"] == state:
            new_dictionary.append(date)

    if new_dictionary != [{}]:
        return new_dictionary[1:]
    else:
        return print("Не верно введен state")


def sort_by_date(dictionary: list[dict], ascending=True) -> list[dict]:
    """Функция, которая возвращает новый список, отсортированный по дате"""
    try:
        if ascending is False:
            return sorted(dictionary, key=lambda ascending: ascending["date"])
        else:
            return sorted(
                dictionary, key=lambda ascending: ascending["date"], reverse=True
            )
    except Exception:
        print("Ошибка в дате")
        raise Exception
