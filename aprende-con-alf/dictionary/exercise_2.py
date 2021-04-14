name = input("What's is your name? ").lower()
age = int(input("What's is your age? "))
address = input("What's is your address? ").lower()
phone_number = int(input("What's is your phone number? "))

dic = {
    'name': name,
    'age': age,
    'address': address,
    'phone_number': phone_number
}

print(f'{dic['name'] has {dic['age'] years old, live i n {dic['address']} a nd your phone number i s {dic['phone_number']}')