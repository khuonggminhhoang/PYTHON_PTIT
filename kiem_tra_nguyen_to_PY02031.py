from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            if isPrime(a[i][j]):
                a[i][j] = 1
            else:
                a[i][j] = 0
    
    for x in a:
        for y in x:
            print(y, end=' ')
        print()