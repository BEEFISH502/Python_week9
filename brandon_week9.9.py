# write a program that evaluates two numbers and decides which of the two is smaller

def smaller(a,b):
    #decide which of two inputss is smaller.
    if a < b:
        min = a
    else:
        min = b
    print(f'Smaller Number: {min}')

smaller(float(input('Enter number: ')), float(input('Enter number: ')))