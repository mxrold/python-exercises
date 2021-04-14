word = input('Enter a word: ').lower()
new_word = list(word)

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
for i in new_word:
    for n in vowels:
        if i == n:
            count += 1

print(f'The word have {count} vowels')
