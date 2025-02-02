def get_mask_card_number(card_number: int) -> str:
    """Функция, которая принимает на вход номер карты и возвращает её маску"""
    card_number = str(card_number)
    new_mask_card = card_number[:4] + ' ' + card_number[6:8] + '** ****' + ' ' + card_number[-4:]
    return new_mask_card


def get_mask_account(card_number: int) -> str:
    """Функция, которая принимает на вход номер счёта и возвращает его маску"""
    card_number = str(card_number)
    return '**' + card_number[-4:]


print(get_mask_card_number(input()))
print(get_mask_account(input()))
