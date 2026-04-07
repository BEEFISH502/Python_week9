# write a program that converts celsius to Fahrenheit
# define the function
def f_to_c():
    #calculate fahrenheit to celsius
    f = float(input('Enter temperature in F: '))
    c = (f - 32) * 5/9
    return c

c = f_to_c()
print(f'Temperature in C: {c:.1f}')

