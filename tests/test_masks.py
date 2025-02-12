import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_card_number",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("1234567887654321", "1234 56** **** 4321"),
    ],
)
def test_get_mask_card_number(card_number, mask_card_number):
    """Тест на правильность маскирования номера карты."""
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize(
    "card_number_vrong",
    [
        ("-548714"),
        ("548*555"),
        ("54587122569851jkhgfft26548"),
        ("zero"),
        (""),
    ],
)
def test_get_mask_card_number_vrong(card_number_vrong):
    """Тест на правильность ввода номера карты."""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number_vrong)
        assert (
            str(exc_info.value)
            == "Ошибка при ввводе номера карты.Введите правильный номер карты:"
        )


@pytest.mark.parametrize(
    "account, mask_account",
    [
        ("11111111111111111111", "**1111"),
        ("54968752315874698725", "**8725"),
        ("95874125639875412365", "**2365"),
    ],
)
def test_get_mask_account(account, mask_account):
    """Тест на правильность маскирования счета"""
    assert get_mask_account(account) == mask_account


@pytest.mark.parametrize(
    "account_vrong",
    [("54874"), ("jhjgdf5641546"), (""), ("854789652154898565248565525")],
)
def test_test_get_mask_account_vrong(account_vrong):
    """Тест на правильность ввода номера счета."""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_vrong)
        assert (
            str(exc_info.value)
            == "Ошибка при вводе номера счета. Введите правильный номер счета:"
        )
