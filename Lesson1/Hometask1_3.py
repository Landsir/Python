# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
#(или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
         
x = float(input('input x, not equal to 0: '))            
y = float(input('input y, not equal to 0: '))

if x == 0 or y == 0:
        print ('error')
else: 
    if x>0 and y>0:
        text = 'I'
    elif x > 0 and y <  0:
                text = 'IV'
    elif x < 0 and y > 0:
                text = 'II'
    elif x <0 and y<0:
                text = 'III'
    print(f"the coordinate point is in the {text} quadrant")





