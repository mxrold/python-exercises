annual_rent = float(input("What's your annual rent? "))

if annual_rent < 10000:
    print('Tax rate: 5%')
elif annual_rent >= 10000 and annual_rent < 20000:
    print('Tax rate: 15%')
elif annual_rent >= 20000 and annual_rent < 35000:
    print('Tax rate: 20%')
elif annual_rent >= 35000 and annual_rent < 60000:
    print('Tax rate: 30%')
elif annual_rent >= 60000:
    print('Tax rate: 45%')
else:
    print('Error')
