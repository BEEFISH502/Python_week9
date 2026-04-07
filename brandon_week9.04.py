# write a program that formats names

#define the function
def format_name(first,last):
    #takes first last name format them neatly into standard format
    if first and last:
        return f'{first.title()} {last.title()}'

## call function
first = input('Enter first name: ')
last = input('Enter last name: ')
name = format_name(first, last)
print(f'Formatted name: {name}')

