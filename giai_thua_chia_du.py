from math import *

fac = [1] * (10 ** 6 +1) 
def init():
    for i in range(2, 10 ** 6 + 1):
        fac[i] = fac[i-1] * i
        fac[i] %= (10 ** 9 +1)

if __name__ == '__main__':
    init()
    n = int(input())
    while n != 0:
        print(fac[int(input())])
        n-=1 