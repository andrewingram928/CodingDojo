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


guido = User("Guido")
monty = User("Monty")
andrew = User("Andrew")

guido.make_deposit(100)
guido.make_deposit(50)
guido.make_deposit(125)
guido.make_withdrawal(100)
guido.display_user_balance()

monty.make_deposit(60)
monty.make_deposit(90)
monty.make_withdrawal(20)
monty.make_withdrawal(60)
monty.display_user_balance()

andrew.make_deposit(20)
andrew.make_deposit(260)
andrew.make_deposit(30)
andrew.make_withdrawal(500)
andrew.display_user_balance()

guido.transfer_money(andrew, 100)
