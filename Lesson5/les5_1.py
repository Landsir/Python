# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". 
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке
# и False - в противном случае.


f = open('les5.txt', 'w')
path  = 'абв слова слоабв крокодил'
f.writelines(path)
f.close()

f = open('les5.txt', 'r')
text = f.readline().split()
print([i for i in text if 'абв' not in i])
f.close()