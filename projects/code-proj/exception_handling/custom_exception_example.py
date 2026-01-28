class Amount:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return repr((self.currency,self.amount))

    def add(self, that):
        if(self.currency == that.currency):
            self.amount += that.amount
        else:
            raise CurrencyDoNotMatch(self.currency + ' ' + that.currency)


class CurrencyDoNotMatch(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

amount1 = Amount('EUR',2)
amount2 = Amount('INR',4)

amount2.add(amount1) # CurrencyDoNotMatch: INR EUR
print(amount1)
print(amount2)
