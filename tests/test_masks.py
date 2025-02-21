import pytest

from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    """Тест функции get_mask_card_number"""
    #Номер карты нормального значения
    assert get_mask_card_number("7000792289606361") == '7000 79** **** 6361'

    #Номер карты с меньшим значением (меньше 16 символов)
    assert get_mask_card_number("700079228960") == '7000 79** **** 8960'

    #Номер карты с большим значением (больше 16 символов)
    assert get_mask_card_number("70007922896063618091") == '7000 79** **** 8091'

    #Вместо номера карты пустое значение
    assert get_mask_card_number("") == " ** **** "
