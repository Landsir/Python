# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('input a number: '))
list1=[0,1]
list2 = [-1,1]
i = 0
a = 0
while i < k-1:
    list1.append(list1[i]+list1[i+1])
    i+=1
    list2.insert(0, (list2[a+1]-list2[a]))
    print(list2)
    
print(list2+list1)