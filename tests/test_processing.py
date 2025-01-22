import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(dictionary):
    """Тест на фильтрацию списка по значению ключа state, принятом по умолчанию (EXECUTED)."""
    assert filter_by_state(dictionary, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_canceled(dictionary):
    """Тест на фильтрацию списка по значению ключа state, принятом по умолчанию (CANCELED)."""
    assert filter_by_state(dictionary, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "invalid_state",
    [
        ({"id": 41428829, "state": "hgfhyjh", "date": "2019-07-03T18:35:29.512364"}),
        (
            {
                "id": 939719570,
                "state": " -gjs455  ",
                "date": "2018-06-30T02:08:58.425572",
            }
        ),
        ({"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"}),
        ({"id": 594226727, "date": "2024-03-11T02:26:18.671407"}),
    ],
)
def test_filter_by_state_invalid_state(invalid_state):
    """Тест на некорректное значение ключа state."""
    with pytest.raises(TypeError):
        filter_by_state(invalid_state)


def test_sort_by_date_true(dictionary):
    """Тест на фильтр данных по дате True/Убывание"""
    assert sort_by_date(dictionary, True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_false(dictionary):
    """Тест на фильтр данных по дате False/Возростание"""
    assert sort_by_date(dictionary, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.parametrize(
    "vrong_date",
    [
        {"id": 939719570, "state": "EXECUTED", "date": "20-06-0T02:8:58.42552"},
        {"id": 594226727, "state": "CANCELED", "date": "20125.241689"},
        {"id": 615064591, "state": "CANCELED", "date": ""},
        {"id": 41428829, "state": "EXECUTED", "date": "ffdgd/fgd/"},
    ],
)
def test_sort_by_date_vrong(vrong_date):
    """Тест на фильтр неправильной дате"""
    with pytest.raises(Exception) as exc_info:
        sort_by_date(vrong_date)
        assert str(exc_info.exception) == "Ошибка в дате"
