class User:
    def __init__(self, name):
        self.name = name
        self.checkings = checkings(int_rate = 1.02 , balance = 0)
        self.savings = savings(int_rate = 1.03, balance= 0)

class checkings:
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

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.checkings.balance += amount
        other_user.checkings.display_account_info()
        self.display_account_info()
        return self

class savings:
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

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.checkings.balance += amount
        other_user.checkings.display_account_info()
        self.display_account_info()
        return self

guido = User("Guido")
monty = User("Monty")
andrew = User("Andrew")

andrew.savings.display_account_info().deposit(100).deposit(1000).transfer_money(guido, 500)

andrew.checkings.display_account_info()