number = int(input('Enter a number: '))

i = 2
while number % i != 0:
    print(i)
if i == number:
    print(str(number) + ' is prime')
else:
    print(str(number) + ' is not prime')