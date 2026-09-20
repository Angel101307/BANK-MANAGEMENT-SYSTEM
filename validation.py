def validate_account_number(number):
    """Check whether the account number contains exactly 5 digits."""
    return len(number) == 5 and number.isdigit()


def validate_mobile(number):
    """Check whether the mobile number contains exactly 10 digits."""
    return len(number) == 10 and number.isdigit()


def get_positive_amount(prompt):
    """Accept only a valid positive monetary amount."""

    while True:
        try:
            amount = float(input(prompt))

            if amount <= 0:
                print("AMOUNT MUST BE GREATER THAN ZERO.")
                continue

            return amount

        except ValueError:
            print("PLEASE ENTER A VALID NUMBER.")
