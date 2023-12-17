from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    sum = sum(a)
    sumleft = 0
    for i in range(1,n):
        sumleft += a[i-1]
        if isPrime(sumleft) and isPrime(sum - sumleft - a[i]):
            print(i, end=' ')
        