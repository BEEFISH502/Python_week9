# write a program that evaluates price and quantity and prints a total

def line_total(price,qty):
    total = price * qty
    print(f'Line Total: ${total:.2f}')

line_total(float(input('Enter item price: ')), int(input('Enter quantity: ')))

