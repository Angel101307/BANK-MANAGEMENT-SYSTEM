class Account:
    """Stores basic customer account information."""

    def __init__(self, name, account_number, mobile, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.mobile = mobile
        self.balance = balance
        self.history = []

    def add_history(self, transaction):
        self.history.append(transaction)
