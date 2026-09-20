from account import Account
from validation import validate_account_number
from validation import validate_mobile


def test_account_validation():

    assert validate_account_number("12345") is True
    assert validate_account_number("1234") is False
    assert validate_account_number("123456") is False
    assert validate_account_number("12A45") is False


def test_mobile_validation():

    assert validate_mobile("9876543210") is True
    assert validate_mobile("987654321") is False
    assert validate_mobile("98765432101") is False
    assert validate_mobile("98765ABCDE") is False


def test_account_creation():

    account = Account(
        "Angel",
        "12345",
        "9876543210",
        5800.43
    )

    assert account.name == "Angel"
    assert account.account_number == "12345"
    assert account.balance == 5800.43


if __name__ == "__main__":

    test_account_validation()
    test_mobile_validation()
    test_account_creation()

    print("ALL BASIC TESTS PASSED.")
