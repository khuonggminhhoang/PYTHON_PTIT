from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    a = list(map(int, input().split())) 
    dct = dict()
    for x in a:
        if isPrime(x):
            if x in dct:
                dct[x] += 1 
            else:
                dct[x] = 1
    for key, val in dct.items():
        print(key, val)
    