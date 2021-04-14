investment = float(input('Enter the investment amount: '))
interest = float(input('Enter annual porcentage: '))
years = float(input('Enter numbers of years to investment: '))

result = round(investment * (interest / 100 + 1)**years, 2)

print('The capital obtained in the investment is ' + str(result))