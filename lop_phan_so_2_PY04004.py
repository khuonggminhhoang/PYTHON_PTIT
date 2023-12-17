from math import *

class PhanSo:
    def __init__(self, tu, mau):
        self.__tu = tu
        self.__mau = mau
        
    def add(self, other):
        tu = self.__tu * other.__mau + self.__mau * other.__tu
        mau = self.__mau * other.__mau
        tmp = gcd(tu, mau)
        tu //= tmp
        mau //= tmp
        return PhanSo(tu, mau)

    def __str__(self):
        return str(self.__tu) + '/' + str(self.__mau)

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    p1 = PhanSo(arr[0], arr[1])
    p2 = PhanSo(arr[2] , arr[3])
    p = p1.add(p2)
    print(p)
