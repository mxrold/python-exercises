name = input("What's is your name? ").lower()
gender =  input("What's is your gender? M or F: ").lower()

if name < 'm' and gender == 'f':
    print('Group: A')
elif name > 'n' and gender == 'm':
    print('Group: A')
else:
    print('Group: B')
