foreign_exc = {
    'euro':'€', 
    'dollar':'$', 
    'yen':'¥'
}

menu = """
What foreing exchange do you want? 

Press:
1- Euro
2- Dollar
3- Yen

"""
ask_exc = int(input(menu))

if ask_exc == 1:
    print(foreign_exc['euro'])
elif ask_exc == 2:
    print(foreign_exc['dollar'])
elif ask_exc == 3:
    print(foreign_exc['yen'])
else:
    print('Upps. Error')