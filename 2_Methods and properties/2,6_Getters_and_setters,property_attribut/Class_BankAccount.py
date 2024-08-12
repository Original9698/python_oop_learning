class BankAccount:
    def __init__(self, _account_number, _balance):
        self._account_number = _account_number
        self._balance = _balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        self._balance = value

    account_number = property(fget=get_account_number)
    balance = property(fget=get_balance, fset=set_balance)
