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

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        other_user.display_user_balance()
        self.display_user_balance()
        return self


guido = User("Guido")
monty = User("Monty")
andrew = User("Andrew")

guido.make_deposit(100).make_deposit(50).make_deposit(125).make_withdrawal(100).display_user_balance()

monty.make_deposit(60).make_deposit(90).make_withdrawal(20).make_withdrawal(60).display_user_balance()

andrew.make_deposit(20).make_deposit(260).make_deposit(30).make_withdrawal(500).display_user_balance()

guido.transfer_money(andrew, 100)