# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число
# будем искать число 3 в одной из строк списка. 

spisok = ["случайная строка1", "случаная строка2", "случайная строка3"]
print(any('3' in row for row in spisok))
