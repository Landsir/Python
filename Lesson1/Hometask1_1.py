# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Input a number of a week day '))
if day > 7:
     print('incorrect number')
elif day == 6 or day==7:
     print("it's a holiday, let's have a drink")
else: print("this is a working day, work harder")

