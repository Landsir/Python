# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math
my_list = [2,3,4,5,6]
print(my_list)
new_list =[]
i=0
k=len(my_list)

while i <= math.ceil(k/2):
    mult = my_list[i]*my_list[k-1]
    i+=1
    k-=1
    new_list.append(mult)
print(new_list)
    