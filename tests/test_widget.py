import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card(card_zero, card_account, card_visa, card_another):
    assert mask_account_card("0") == card_zero
    assert mask_account_card("Счет 12345678901234567890") == card_account
    assert mask_account_card("Visa 1234567890123456") == card_visa
    assert mask_account_card("Visa Super Puper 1234567890123456") == card_another


def test_get_date(date_get, date_zero, date_slash):
    assert get_date("2012-11-10T01:02:03.012345") == date_get
    assert get_date("0") == date_zero
    assert get_date("2012/11/10T01:02:03.012345") == date_slash