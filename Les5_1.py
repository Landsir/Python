# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = (input('Input a text: ').split())
print([i for i in text if 'абв' not in i])
