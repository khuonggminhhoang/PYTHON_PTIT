from math import *

class PhanSo:
    def __init__(self, tu, mau):
        self.__tu = tu
        self.__mau = mau
    
    def __str__(self):
        tmp = gcd(self.__tu, self.__mau)
        self.__tu //= tmp
        self.__mau //= tmp
        return f'{self.__tu}/{self.__mau}'

if __name__ == '__main__':
    tu, mau = map(int, input().split())
    p = PhanSo(tu, mau)
    print(p)