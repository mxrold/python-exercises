password = 'example'
ask_password = input('Enter a password: ').lower()

if password == ask_password:
    print('The passwords are equals. Welcome!')
else:
    print("The passwords aren't equals. Try again")