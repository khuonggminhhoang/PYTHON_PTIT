from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    t = int(input())
    while t :
        s = input()
        print('YES' if isPrime(int(s[:3])) and isPrime(int(s[(len(s) - 3) : len(s)])) else 'NO')
        t -= 1