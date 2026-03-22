# write a function that calculates tips
#define function
def calc_tip(bill,percent):
    tip = bill * (percent / 100)
    print(f'Tip amount: {tip}')
    return tip

calc_tip(
    bill=float(input('Enter bill amount: ')),
    percent=float(input('Enter tip percent: '))
)
