INT = 4

ask_user = float(input('How much do you want to deposit?: '))

balance_one = (ask_user * 4) / 100 + ask_user
balance_two = (balance_one * 4) / 100 + ask_user
balance_three = (balance_two * 4) / 100 + ask_user

print(f'Your balance is: {str(ask_user)}')
print(f'Your balance in the first year is: {str(balance_one)}')
print(f'Your balance in the second year is: {str(balance_two)}')
print(f'Your balance in the third is: {str(balance_three)}')
