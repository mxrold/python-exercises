weight = float(input('Enter your weight in kilograms: '))
height = float(input('Enter your height in centimetres: '))
height_in_meters = height / 100

imc = round(weight / (height_in_meters)**2, 2)

print('Your body mass index is: ' + str(imc))