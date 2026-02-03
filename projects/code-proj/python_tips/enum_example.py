from enum import Enum

class Currency(Enum):
    USD = 1
    EUR = 2
    INR = 3

for currency in Currency:
    print(currency)
# Currency.USD
# Currency.EUR
# Currency.INR
print('=========')

for currency in Currency:
    print(currency.name , currency.value)
# USD 1
# EUR 2
# INR 3

print('=========')
print(Currency(1), Currency(1).name, Currency(1).value) # Currency.USD USD 1
