number_1 = float(input('Enter first number: '))
number_2 = float(input('Enter second number: '))

if number_1 and number_2:
    result = round(number_1 / number_2, 2)
    print(f'The result of divisition is {result}')
elif number_1 == 0 or number_2 == 0:
    print("Cannot be dividid by zero. Try again")
else:
    print('Error')
