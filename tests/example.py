from src.widget import get_date, mask_account_card

print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_mask_account_card():
    assert (
        mask_account_card("Visa Platinum 7000792289606361")
        == "Visa Platinum 7000 79** **** 6361"
    )


test_get_date()
test_mask_account_card()
