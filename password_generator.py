import random


print('''
********************************
Welcome To My Password Generator
********************************
''')


characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*().,?'

number = int(input('Amount of passwords to generate: '))
length = int(input('Your password length: '))

print('Your passwords:\n')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(characters)
    print(passwords)