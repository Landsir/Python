#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n = int(input('input n '))
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {lst}\n сумма: {round(sum(lst), 3)}')

# n=int(input())
# summ = 0
# for i in range(1, n+1):
#     summ +=(1+1/i)**i
#     print(summ)
# print(summ)