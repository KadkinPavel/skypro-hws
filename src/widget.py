from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Функция, которая обрабатывает информацию как о картах, так и о счетах"""
    parts = card_info.split()

    if "Счет" in parts:
        account_number = parts[-1]
        masked_number = get_mask_account(account_number)
        return f"{' '.join(parts[:-1])} {masked_number}"
    else:
        card_name = " ".join(parts[:-1])
        card_number = parts[-1]
        masked_number = get_mask_card_number(card_number)
        return f"{card_name} {masked_number}"


def get_date(date: str) -> str:
    new_date = date.split("-")
    return f"{new_date[2][:2]}.{new_date[1]}.{new_date[0]}"


