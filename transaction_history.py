def show_history(account):

    print("\n--- TRANSACTION HISTORY ---")

    if len(account.history) == 0:
        print("NO TRANSACTIONS HAVE BEEN MADE YET.")
        return

    for number, transaction in enumerate(
        account.history, start=1
    ):
        print(f"{number}. {transaction}")
