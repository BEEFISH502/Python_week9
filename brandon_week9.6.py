# write a program that determines if a customer has a coupon or not, then adds a discount if True

def final_price(price, has_coupon):
    if has_coupon == 'y':
        price = price * 0.90
        print(f'Final price: {price}')


final_price(float(input('Enter item price: ')),input('Do you have a coupon? (y/n): '))