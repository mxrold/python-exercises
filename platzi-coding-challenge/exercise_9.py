import random


def play_game(number, secret_number):
    count = 0

    while number != secret_number:
        if number < secret_number:
            print('The secret number is higher')
            number = int(input("Enter number "))
            count += 1
        elif number > secret_number:
            print('The secret number is less')
            number = int(input("Enter number "))
            count += 1
        
    print('Good work!!! You discovered the secret number. It was ' + str(secret_number) + ' and you did it in ' + str(count))


def run():
    number = int(input("Enter number "))
    secret_number = random.randint(1, 100)

    return play_game(number, secret_number)


if __name__ == "__main__":
    run()