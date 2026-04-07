# write a program that evaluates price and quantity and prints a total

def line_total(price,qty):
    return price * qty

price = float(input('Enter item price: '))
qty = int(input('Enter quantity: '))
total = line_total(price,qty)
print(f'Line total: ${total:.2f}')


