from math import *

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def distance(self, other):
        return sqrt((self.__x - other.__x) **2 + (self.__y - other.__y) ** 2)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3

    def is_valid(self):
        a = self.__p1.distance(self.__p2)
        b = self.__p1.distance(self.__p3)
        c = self.__p2.distance(self.__p3)
        if ((a + b) > c) and ((a + c) > b) and ((b + c) > a) :
            return True
        return False
    
    def area(self):
        a = self.__p1.distance(self.__p2)
        b = self.__p1.distance(self.__p3)
        c = self.__p2.distance(self.__p3)
        return 0.25 * sqrt((a + b + c) * (a + b - c) * (-a + b + c) * (a - b + c)) 

if __name__ == '__main__':
    t = int(input())
    a = []
    for _ in range(t):
        a += [float(i) for i in input().split()]
    i = 0
    for _ in range(t):
        p1 = Point(a[i], a[i + 1])
        p2 = Point(a[i + 2], a[i + 3])
        p3 = Point(a[i + 4], a[i + 5])
        tri = Triangle(p1, p2, p3)
        i += 6
        if tri.is_valid():
            print('{:.2f}'.format(tri.area()))
        else:
            print('INVALID')