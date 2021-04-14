def traslator(ask_user):
    vowels = ('a', 'e', 'i', 'o', 'u')

    for i in vowels:
        if ask_user[0] != i:
            result = ask_user[1:] + ask_user[0] + "ay"
            return result
        elif ask_user[0] == i:
            return ask_user + "way"


def run():
    ask_user = str(input("Enter a phrase or a word: ")).lower()
    user = traslator(ask_user)
    print(user)
   

if __name__ == "__main__":
    run()