# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел. 
# Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа,
# то есть, стоят вслед за меньшим числом.

# Формат входных данных
# На вход программе подается строка текста из разделенных пробелами натуральных чисел.

# Формат выходных данных
# Программа должна вывести одно число – количество элементов списка, больших предыдущего.

# Тестовые данные 
# Sample Input 1:
# 1 2 3 4 5
# Sample Output 1:
# 4
# Sample Input 2:
# 1 1 3 2 2 1 1 1 1
# Sample Output 2:
# 1
# Sample Input 3:
# 5 4 3 2 1
# Sample Output 3:
# 0

g= list(map(int, input().split()))
t=0
for i in range(1,len(g)):
    if g[i]>g[i-1]:
        t=t+1
print(t)