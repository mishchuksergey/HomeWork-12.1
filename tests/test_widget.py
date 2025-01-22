import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_user, separated",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card(input_user, separated):
    """Тест на проверку разделения входных данных: карта/счет"""
    assert mask_account_card(input_user) == separated


@pytest.mark.parametrize(
    "input_user_vrong",
    [("1"), ("Счкеит 56461315 kjb"), ("Visa 451315 fd56b")],
)
def test_mask_account_card_invalid(input_user_vrong):
    """Тест на правильность ввода данных карты"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(input_user_vrong)
        assert str(exc_info.value) == "Ошибка при ввводе данных"


def test_get_date():
    """Тест на правильность преобразования даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
