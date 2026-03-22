# write a program that formats names

#define the function
def format_name(first,last):
    #takes first last name format them neatly into standard format
    if first and last:
        first = first.title()
        last = last.title()
    ## format and print
    print(f'{first} {last}')



## call function
format_name(input('First name: '), input('Last name: '))
