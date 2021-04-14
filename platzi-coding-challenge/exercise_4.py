def run():
    string = input("Enter a phrase or word ")
    multiply = int(input("How much are you want to multiply this? "))

    if multiply > 0:
        result = (string + ' ') * multiply
        print(result)

if __name__ == "__main__":
    run()