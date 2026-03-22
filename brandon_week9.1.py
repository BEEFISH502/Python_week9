# write a function that calculates tax on a given amount

def calc_tax(amount):
    tax = amount * 0.08
    total = tax + amount
    print(f'Tax: {tax}\nTotal: {total}')
    return tax

# call function, pass an argument (amount)
calc_tax(amount=float(input('Enter purchase amount: ')))