from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n, x = map(int,input().split())

    print(x, end=' ')
    id = 0
    i = 2
    while id < n:
        if isPrime(i):
            x += i
            print(x, end=' ')
            id += 1
        i += 1
