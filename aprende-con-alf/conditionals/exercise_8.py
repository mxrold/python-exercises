scores = float(input("What's the scores? "))

unacceptable = 0
acceptable = 0.4
meritorious = 0.6
money = 2400

if scores >= unacceptable and scores < acceptable:
    print(f'Your score is the {unacceptable} and you salary is {money}')
elif scores >= acceptable and scores < meritorious:
    print(f'Your score is the {acceptable} and you salary is {(money * acceptable) + money}')
elif scores >= meritorious:
    print(f'Your score is the {meritorious} and you salary is {(money * meritorious) + money}')
else:
    print('Error')