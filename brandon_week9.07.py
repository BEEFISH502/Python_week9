# write a program that evaluates text and returns amount of characters

def count_chars(text):
    return len(text)


text = input('Enter a message: ')
chars = count_chars(text)
print(f'Character count: {chars}')


