from account import Account
from validation import validate_account_number, validate_mobile
from transactions import deposit, withdraw
from transfer import transfer_money
from complaints import register_issue
from transaction_history import show_history


def display_menu():
    print("\n" + "=" * 45)
    print("        BANK MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. CHECK BANK BALANCE")
    print("2. WITHDRAW MONEY")
    print("3. DEPOSIT MONEY")
    print("4. MONEY TRANSFER")
    print("5. VIEW TRANSACTION HISTORY")
    print("6. REPORT AN ISSUE")
    print("7. GOODBYE")
    print("=" * 45)


def create_account():
    print("HELLO USER")

    name = input("PLEASE ENTER YOUR NAME: ").strip()

    while True:
        number = input(
            "PLEASE ENTER YOUR 5 DIGIT ACCOUNT NUMBER: "
        ).strip()

        if validate_account_number(number):
            break

        print("PLEASE ENTER A VALID 5 DIGIT ACCOUNT NUMBER.")

    while True:
        mobile = input(
            "PLEASE ENTER YOUR 10 DIGIT MOBILE NUMBER: "
        ).strip()

        if validate_mobile(mobile):
            break

        print("PLEASE ENTER A VALID 10 DIGIT MOBILE NUMBER.")

    return Account(name, number, mobile, 5800.43)


def main():
    account = create_account()

    while True:
        display_menu()

        try:
            choice = int(input("ENTER (1-7): "))
        except ValueError:
            print("PLEASE ENTER A NUMBER FROM 1 TO 7.")
            continue

        if choice == 1:
            print(f"YOUR BANK BALANCE IS: ₹{account.balance:.2f}")

        elif choice == 2:
            withdraw(account)

        elif choice == 3:
            deposit(account)

        elif choice == 4:
            transfer_money(account)

        elif choice == 5:
            show_history(account)

        elif choice == 6:
            register_issue(account)

        elif choice == 7:
            print(f"THANKS FOR VISITING, {account.name}!")
            print("VISIT US AGAIN!!")
            break

        else:
            print("PLEASE ENTER A CORRECT OPTION (1-7).")


if __name__ == "__main__":
    main()
