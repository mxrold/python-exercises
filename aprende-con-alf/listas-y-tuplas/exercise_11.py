list_1 = [1,2,3]
list_2 = [-1,0,2]

product = 0

for i in range(len(list_1)):
    product += list_1[i] * list_2[i]

print(f'The result is {product}')