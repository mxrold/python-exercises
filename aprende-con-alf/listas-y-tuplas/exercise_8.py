ask_user = input('Enter a word: ').strip()

if ask_user == ask_user[::-1]:
    print('It is palindrome')
else:
    print('It is not palindrome')
