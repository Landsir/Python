print('Input a')
a = int(input())
print('Input b')
b= int(input())
if b == a*a:
    print(f'the number {b} is the square of the number {a} ')
elif a == b*b:
    print (f'the number {a} is the square of the number {b}')
else:
    print (f'numbers {a} and {b} are not squares each other')