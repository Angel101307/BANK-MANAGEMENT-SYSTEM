from validation import get_positive_amount


def deposit(account):
    amount = get_positive_amount(
        "ENTER AMOUNT TO BE DEPOSITED: ₹"
    )

    account.balance += amount

    account.add_history(
        f"Deposited ₹{amount:.2f}"
    )

    print(f"₹{amount:.2f} HAS BEEN DEPOSITED SUCCESSFULLY.")
    print(f"UPDATED BALANCE IS: ₹{account.balance:.2f}")


def withdraw(account):
    amount = get_positive_amount(
        "ENTER AMOUNT TO BE WITHDRAWN: ₹"
    )

    if amount > account.balance:
        print("NOT ENOUGH BALANCE.")
        return

    account.balance -= amount

    account.add_history(
        f"Withdrawn ₹{amount:.2f}"
    )

    print(f"₹{amount:.2f} HAS BEEN WITHDRAWN SUCCESSFULLY.")
    print(f"UPDATED BALANCE IS: ₹{account.balance:.2f}")
