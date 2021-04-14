ask_user = input('Enter a password: ')
secret = 'password'

count = 0
while ask_user != secret:
    ask_user = input('Enter a password again: ')
    count += 1


print(f'Welcome. You had {count} tries')


