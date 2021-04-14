import math

def run():
    height = float(input("Enter height "))
    radio = float(input("Enter radio "))

    formula = round(math.pi * radio**2 * height, 1)

    print("The cylinder volume is " + str(formula) + " m3")


if __name__ == "__main__":
    run()