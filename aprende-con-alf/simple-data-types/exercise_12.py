clown = int(input('Enter the amount of clowns: '))
doll = int(input('Enter the amount of dolls: '))

wight_clown = 112
wight_doll = 75

result = (clown * wight_clown) + (doll * wight_doll)

if result >= 1000:
    print('The total wight of the package is ' + str(result / 1000) + ' kilograms')
else:
    print('The total wight of the package is ' + str(result) + ' grams')
