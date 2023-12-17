from math import *

def isPrime(n):
    if n < 2 : return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    cnt = 0
    for x in a:
        if isPrime(x):
            cnt += 1
            sum += x

    print('%.3f' %(sum/cnt))
