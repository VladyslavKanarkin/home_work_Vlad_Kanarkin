
EXCHANGE_RATES = {
    "EUR": 50.1,
    "USD": 45.1,
    "UAN": 30.1
}

def check(currency):
    if currency not in EXCHANGE_RATES: raise ValueError("Неизвестная валюта " + currency)

def convert(curr_from, curr_to, amount):
    check(curr_from); check(curr_to)
    return amount * EXCHANGE_RATES[curr_from] / EXCHANGE_RATES[curr_to]

cf = input('Currency1:')
ct = input('Currency2:')
amt = int(input('Quantity:'))

print(convert(cf, ct, amt))