from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n %i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    t = int(input())
    while t :
        s = input()
        ans = int(s[len(s) - 4 : len(s)])
        print('YES' if isPrime(ans) else 'NO')
        t -= 1