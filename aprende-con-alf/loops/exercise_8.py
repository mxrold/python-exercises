number = int(input('Enter a number: '))

for i in range(1, number+1, 2):
    for n in range(i, 0, -2):
        print(n, end=" ")
    
    print("")