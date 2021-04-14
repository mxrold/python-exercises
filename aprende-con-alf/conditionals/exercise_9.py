age_user = int(input("What's your age? "))


if age_user < 4:
    print('You can to entrance free')
elif age_user >= 4 and age_user < 18:
    print('You must to pay 5€')
else:
    print('You must to pay 10€')

