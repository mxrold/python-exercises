def run(types_pizza):
    response = 'Your pizza has the ingredients: Mozzarella, tomato and '

    if types_pizza == 1:
        ask_user = """
        Press for select ingredients:

        1- Bell pepper(pimiento)
        2- Tofu
        
        """
        sel_ing = int(input(ask_user))
        if sel_ing == 1:
            print(response + 'bell pepper')
        elif sel_ing == 2:
            print(response + 'tofu')
        else:
            print('Error 1')
    elif types_pizza == 2:
        ask_user = """
        Press for select ingredients:

        1- Pepperoni
        2- Ham (Jamón)
        3- Salmon

        """
        sel_ing = int(input(ask_user))
        if sel_ing == 1:
            print(response + 'pepperoni')
        elif sel_ing == 2:
            print(response + 'ham')
        elif sel_ing == 3:
            print(response + 'salmon')
        else:
            print('Error 2')
    else:
        print('Error 3')


if __name__ == "__main__":
    menu_pizza = """
    What pizza do you want?

    Press for select:
    1- Vegetarian
    2- No vegetarian

    """
    types_pizza = int(input(menu_pizza))
    run(types_pizza)