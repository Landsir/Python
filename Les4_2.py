#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int(input())
my_list = []
i=2
while i <= n:
    if (n%i) == 0:
        my_list.append(i) 
        n //=i
        i = 2
    else:
        i+=1
        
print(my_list)
            
        
        
    