# write a program that determines if a customer has a coupon or not, then adds a discount if True

def final_price(price, has_coupon):
    if has_coupon == 'y':
        price = price * 0.90
        return price
    else:
        return price

price = float(input('Enter item price: '))
has_coupon = input('Do you have a coupon? (y/n): ')
total = final_price(price,has_coupon)
print(f'Final price: {total:.1f}')