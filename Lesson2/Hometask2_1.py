#Напишите программу, которая принимает на вход вещественное число и показывает сумму его чисел. 

# num = int(input("Imput a number: "))
# sum = 0
# while (num != 0):
#     sum = sum + num % 10
#     num = num // 10
# print("Sum is: ", sum)

#import random
#a=random.randint(100, 99999)

a = input('input a number: ')
b = map(int, str(a))
print(f'your number is {a}, sum of digits = {sum(b)}')

# s='123'
# summ =0
# for i in s:
#     if i.isdigit():
#         summ =+ int(i)
# print(summ)