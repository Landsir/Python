#дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что любой символ
# в том числе пробел, стоит 60 копеек. Ответ дайте в рублях и копейках. 

line = str(input('input a message '))
cost = len(line)
coins = cost*60
if coins > 100:
    rubls = coins//100
    coins = coins % 100
    print(f'your message costs {rubls} rubls and {coins} coins')
else:
    print(f'your message costs {coins} coins')

