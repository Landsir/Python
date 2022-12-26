# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def ent(x):
    xy = ['x', 'y']
    a = []
    for i in range(x):
        flag = False
        while not flag:
            try:
                number = int(input(f'Input {xy[i]} coordinates: '))
                a.append(number)
                flag = True
            except ValueError:
                print('Error, input integer number' )

    return a

def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print('Input A point coordinates ')
pointA = ent(2)
print('Input B point coordinates ')
pointB = ent(2)

print(f"Segment length is {format(calculateLengthSegment(pointA, pointB), '.2f')}")
