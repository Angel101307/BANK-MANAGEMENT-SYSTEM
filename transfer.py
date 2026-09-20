from validation import validate_account_number
from validation import get_positive_amount


def transfer_money(account):

    receiver = input(
        "ENTER THE RECEIVER'S 5 DIGIT ACCOUNT NUMBER: "
    ).strip()

    if not validate_account_number(receiver):
        print(
            "PLEASE ENTER A VALID 5 DIGIT "
            "RECEIVER ACCOUNT NUMBER."
        )
        return

    if receiver == account.account_number:
        print("YOU CANNOT TRANSFER MONEY TO YOUR OWN ACCOUNT.")
        return

    amount = get_positive_amount(
        "ENTER AMOUNT TO BE TRANSFERRED: ₹"
    )

    if amount > account.balance:
        print("NOT ENOUGH BALANCE.")
        return

    account.balance -= amount

    account.add_history(
        f"Transferred ₹{amount:.2f} to account {receiver}"
    )

    print(
        f"UPDATED BANK BALANCE IS: "
        f"₹{account.balance:.2f}"
    )

    print(
        f"₹{amount:.2f} HAS BEEN TRANSFERRED "
        f"TO {receiver} SUCCESSFULLY."
    )
