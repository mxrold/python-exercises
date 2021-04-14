ask_user = input('Enter a word o phrase: ')
list_word = list(ask_user)
letter = input('Enter a letter: ')


count = 0
for i in list_word:
    if i == letter:
        count += 1
    else:
        break
    
print(f'The letter {letter} was found: {count}')