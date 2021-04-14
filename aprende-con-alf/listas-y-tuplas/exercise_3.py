subjects = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
nota = []

count = 0
while count < len(subjects):
    ask_user = int(input('Enter a note: '))
    nota = ask_user.append()

for i in subjects:
    print(f'En la materia {i} te sacaste {nota}')