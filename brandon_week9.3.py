# write a program that converts celsius to Fahrenheit
# define the function
def f_to_c(f):
    #calculate fahrenheit to celsius
    c = (f - 32) * 5/9
    print(f'Temperature in C: {c}')
    return c

f_to_c(float(input('Enter temperature in F: ')))

