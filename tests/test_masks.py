from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number(card_num):
    assert get_mask_card_number("0") == card_num
    assert get_mask_card_number("abcdefghijkopqr") == card_num


def test_mask_account(account_num):
    assert get_mask_account("0") == account_num
    assert get_mask_account("abcdefghijkopqrs") == account_num