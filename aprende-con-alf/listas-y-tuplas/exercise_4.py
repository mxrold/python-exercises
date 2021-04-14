len_lottery = int(input('How many are the lottery numbers: '))

numbers = []
count = 1
while count < len_lottery + 1:
    ask_user = int(input(f'{count}. Enter a number: '))
    numbers.append(ask_user)
    count += 1

numbers.sort()
print(numbers)
