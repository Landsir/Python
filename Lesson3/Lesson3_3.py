# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#new_list =[]
#my_list = [1.1,1.2,3.1,5.8,10.01]
#for i in my_list:
#    new_list.append(round((i*10)%10,2))
#print(new_list)

#new_list.sort()
#print(f"разница между максимальным {new_list[len(new_list)-1]} и минимальным {new_list[0]} равна {(new_list[len(new_list)-1])-new_list[0]}")

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))