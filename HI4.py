class Payment:
    def __init__(self, balance):
        self.balance = balance

    def display_balance(self):
        print("Balance:", self.balance)


class UPI(Payment):
    def upi_payment(self, amount):
        self.balance -= amount
        print("UPI Payment:", amount)
        self.display_balance()


class Card(Payment):
    def card_payment(self, amount):
        self.balance -= amount
        print("Card Payment:", amount)
        self.display_balance()


u = UPI(10000)
u.upi_payment(2000)

print()

c = Card(10000)
c.card_payment(3000)