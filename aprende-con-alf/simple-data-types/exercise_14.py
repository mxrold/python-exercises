bread = int(input('Enter the amount of bread: '))
old_bread = int(input('Enter the amount of OLD bread: '))

cost_bread = 3.49
cost_old_bread = (cost_bread * 60) / 100

result = round((bread * cost_bread) + (old_bread + cost_old_bread), 2)

print('The total cost is: ' + str(result) + ' €')