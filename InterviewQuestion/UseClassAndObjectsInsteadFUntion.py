
def deposit_fn(current_balance, amount):
    return current_balance + amount

print(deposit_fn(1000, 500))



class BankAccount:

    def __init__(self, current_balance):
        self.balance = current_balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)


obj = BankAccount(1000)
obj.deposit(100)
obj.deposit(200)





