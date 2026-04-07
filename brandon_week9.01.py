# write a function that calculates tax on a given amount

def calc_tax(amount):
    tax = amount * 0.08
    total = tax + amount
    return tax, total

# call functionn, pass an argument (amount)
amount = float(input('Enter purchase amount: '))
tax, total = calc_tax(amount)
print(f'Tax: {tax}\nTotal: {total}')

