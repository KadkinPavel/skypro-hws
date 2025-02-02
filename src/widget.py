from masks.py import get_mask_card_number, get_mask_account
def mask_account_card(card_number:Union[str:int]) -> str:
    """Функция, которая обрабатывает информацию как о картах, так и о счетах"""
    card_number = card_number.split()
    for i in card_number:
        if i.isdigit():
            a = get_mask_card_number()
            break
    return mask_account_card(i)

print(mask_account_card(input()))
