hours_worked = float(input('Enter worked hours: '))
cost_hour = float(input('Enter cost hour worked: '))

result = round(hours_worked * cost_hour, 2)
result = str(result)

print(result)