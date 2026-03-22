# write a program that evaluates text and returns amount of characters

def count_characters(text):
    count = len(text)
    print(f'Character count: {count}')

count_characters(input('Enter a message: '))

