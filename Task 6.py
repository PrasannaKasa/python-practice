class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def display(self):
        print(self.get_balance())


obj = SavingsAccount(50000)
obj.display()
