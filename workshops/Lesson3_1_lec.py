list = [1,2,3,5,8,15,23,38]
def mult (x):
    return x**2
newList = [(i, mult(i) ) for i in list if i%2 == 0 ]
print (newList)