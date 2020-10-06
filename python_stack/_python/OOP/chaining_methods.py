class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name} , Balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        other_user.display_user_balance()
        self.display_user_balance()
        return self

class BankAccount:
    def __init__(self, int_rate = 1.2 , balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Account Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
            return self

guido = User("Guido")
monty = User("Monty")
andrew = User("Andrew")

guido_account = BankAccount(balance = 500)
andrew_account = BankAccount(int_rate = 1.05, balance = 1000)

guido_account.deposit(500).deposit(200).deposit(100).withdraw(700).yield_interest().display_account_info()
andrew_account.deposit(4000).deposit(2000).withdraw(200).withdraw(100).withdraw(700).withdraw(700).yield_interest().display_account_info()

# guido.make_deposit(100).make_deposit(50).make_deposit(125).make_withdrawal(100).display_user_balance()

# monty.make_deposit(60).make_deposit(90).make_withdrawal(20).make_withdrawal(60).display_user_balance()

# andrew.make_deposit(20).make_deposit(260).make_deposit(30).make_withdrawal(500).display_user_balance()

# guido.transfer_money(andrew, 100)