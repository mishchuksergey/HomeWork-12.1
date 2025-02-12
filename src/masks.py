def get_mask_card_number(card_number: str) -> str:
    """функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX"""

    new_card_number = card_number.replace(" ", "")

    if not (len(new_card_number) == 16 and new_card_number.isdigit()):
        raise ValueError(
            "Ошибка при ввводе номера карты.Введите правильный номер карты:"
        )
    mask = "** ****"
    mask_card_number = (
        new_card_number[:4]
        + " "
        + new_card_number[4:6]
        + mask
        + " "
        + new_card_number[12:]
    )
    return mask_card_number


def get_mask_account(account: str) -> str:
    """функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX"""
    if not (len(account) == 20 and account.isdigit()):
        raise ValueError(
            "Ошибка при вводе номера счета. Введите правильный номер счета."
        )
    mask = "**"
    mask_account = mask + account[-4:]
    return mask_account
