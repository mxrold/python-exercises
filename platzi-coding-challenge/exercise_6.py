def calculator(number, ask_operator, number_2):
    if ask_operator == '1':
        print("The sum is " + str(number + number_2))
    elif ask_operator == '2':
        print("The subtraction is " + str(number - number_2))
    elif ask_operator == '3':
        print("The divide is " + str(number / number_2))
    elif ask_operator == '4':
        print("The multiply is " + str(number * number_2))
    else:
        print("Enter a number or operator valid")


def run():
    number = int(input("Enter a number "))
    number_2 = int(input("Enter next number "))
    main_operator = """
    Press:
    1 - Sum
    2 - Subtraction
    3 - Divide
    4 - Multiply """
    ask_operator = str(input(main_operator))

    return calculator(number, ask_operator, number_2)


if __name__ == "__main__":
    run()