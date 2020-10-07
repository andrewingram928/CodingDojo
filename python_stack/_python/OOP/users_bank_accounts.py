class User:
    def __init__(self, name):
        self.name = name
        self.checkings = BankAccount(int_rate = 1.02 , balance = 0)
        self.savings = SavingsAccount(int_rate = 1.03, balance= 0)

    def make_deposit(self, amount, account):
        if account == 'savings':
            self.savings.balance += amount
            return self
        else:
            self.checkings.balance += amount
            return self

    def make_withdrawal(self, amount, account):
        if account == "savings":
            self.savings.balance -= amount
            return self
        else:
            self.checkings.balance -= amount
            return self

    def display_user_balance(self, account):
        if account == "savings":
            print(f"User: {self.name} , Balance: {self.savings.balance}")
            return self
        else:
            print(f"User: {self.name} , Balance: {self.checkings.balance}")
            return self

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

    def yield_interest(self, account):
        if account == "savings":
            if self.savings.balance > 0:
                self.savings.balance = self.savings.balance * self.savings.int_rate
                return self
        else:
            if self.checkings.balance > 0:
                self.checkings.balance = self.checkings.balance * self.checkings.int_rate
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

andrew.display_user_balance("checkings").make_deposit(1000, "checkings").make_withdrawal(500, "savings").yield_interest("checkings").display_user_balance("checkings")