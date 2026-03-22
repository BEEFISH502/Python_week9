# write a program that converts hours to minutes

def to_hours_minutes(total_minutes):
    hours = total_minutes // 60
    leftover = total_minutes % 60
    print(f'That is {hours} hours and {leftover} minutes.')

to_hours_minutes(int(input('Enter total minutes: ')))
