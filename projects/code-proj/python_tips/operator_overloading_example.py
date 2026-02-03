i = 1
j = 2
# print(i+j) # Here i & j are object. In python, everything is object, there is no primitive type

class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __add__(self, other):
        return Money(self.currency, self.amount + other.amount)
    def __sub__(self, other):
        return Money(self.currency, self.amount - other.amount)

    def __repr__(self):
        return repr((self.currency, self.amount))

amount1 = Money('USD', 100)
amount2 = Money('USD', 300)
print(amount1 + amount2) # ('USD', 400)
print(amount1 - amount2) # ('USD', -100)
