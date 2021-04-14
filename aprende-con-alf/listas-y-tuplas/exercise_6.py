subjects = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
qualification = []

for i in subjects:
    ask_user = int(input(f'What is your qualification in {i}: '))
    qualification.append(ask_user)

for n in qualification:
    if n >= 6:
        qualification.remove(n)
    
print(qualification)