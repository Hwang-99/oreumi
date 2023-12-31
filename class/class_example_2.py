class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
account = BankAccount("12345678", 1000000)
print(account._account_number)
print(account.get_balance())