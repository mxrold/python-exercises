def area(base, height):
    formula_area = round((base * height) / 2, 2)

    print("The area of the triangle is " + str(formula_area))


def run():
    base = float(input("Enter base "))
    height = float(input("Enter height "))

    if base < 0 or height < 0:
        print("The number can't be less zero. Try again 😀")
    else: 
        return area(base, height)


if __name__ == "__main__":
    run()
    