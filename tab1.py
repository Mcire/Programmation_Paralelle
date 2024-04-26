import math

# def add(x,y):
#     return x+y

# def multiply(x,y):
#     return x*y

# def diff(x,y):
#     return x-y

def my_map(func, arg1, arg2):
    res = []
    for i, j in zip(arg1,arg2):
        res.append(func(i,j))
    nameOfFunction = func.__name__
    print('Calling function ', nameOfFunction , ' with arguments ', arg1 ,' and ',arg2 ," .\n", res)
    return res

# a=[1,2,3,4,5]
# b=[6,7,8,9,10]

# my_map(add,a,b)
# my_map(multiply,b,a)
# my_map(diff,a,b)

#Exercice 2:
def calc_distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    
    return distance

# Continuation du code précédent

points1 = [(1.0, 1.0, 1.0),(2.0, 2.0, 2.0),(3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0),(5.0, 5.0, 5.0),(6.0, 6.0, 6.0)]

distances = my_map(calc_distance, points1, points2)

print(distances)
