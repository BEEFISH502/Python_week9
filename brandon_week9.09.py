# write a program that evaluates two numbers and decides which of the two is smaller

def smaller(a,b):
    #decide which of two inputss is smaller.
    if a < b:
        min = a
    else:
        min = b
    return min

a = float(input('Enter number 1: '))
b = float(input('Enter number 2: '))

num = smaller(a,b)
print(f'Smaller number: {num:.1f}')