# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input('input the number of a quadrant: '))
if x>4 or x<0:
    print('error')

elif x == 1:
    print('the range of I quadrant is: x > 0 and y > 0')
elif x == 2:
    print ('the range of II quadrant is: x < 0, y > 0')
elif x == 3:
    print ('the range of III quadrant is: x < 0, y < 0')
elif x == 4:
    print ('the range of IV quadrant is: x > 0, y < 0')




