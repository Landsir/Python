# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
import math
number = int(input('input a number: '))

new_number = []
while number != 0:
    new_number.append(number%2)
    number = math.floor(number/2)
new_number.reverse()
for i in new_number:
    print(i, end =' ')