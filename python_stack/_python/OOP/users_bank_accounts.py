class User:
    def __init__(self, name):
        self.name = name
        self.checkings = BankAccount(int_rate = 1.02 , balance = 0)
        self.savings = SavingsAccount(int_rate = 1.03, balance= 0)

    def transfer_money(self, other_user, amount, account):
        if account == "savings":
            self.savings.balance -= amount
            other_user.checkings.balance += amount
            other_user.checkings.display_account_info()
            self.savings.display_account_info()
            return self
        else:
            self.checkings.balance -= amount
            other_user.checkings.balance += amount
            other_user.checkings.display_account_info()
            self.checkings.display_account_info()
            return self

class BankAccount:
    def __init__(self, int_rate = 1.02 , balance = 0):
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

class SavingsAccount:
    def __init__(self, int_rate = 1.03 , balance = 0):
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

andrew.savings.display_account_info()