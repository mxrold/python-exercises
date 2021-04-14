import random


def play_game(ask_user):
    kind_of_play = ('Rock', 'Scissors', 'Paper')
    ask_computer = random.choice(kind_of_play)

    if ask_user  == ask_computer :
        print('You chose: ' + ask_user + ' | Computer chose: ' + str(ask_computer))
    elif ask_user  != ask_computer :
        print('You chose: ' + ask_user + ' | Computer chose: ' + str(ask_computer))


def run():
    menu = """
        Welcome to the game!

        For the play, press any the next numbers:

        - Rock
        - Scissors
        - Paper
    """
    ask_user = str(input(menu)).capitalize()
    
    return play_game(ask_user)


if __name__ == "__main__":
    run()