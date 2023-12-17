from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n %i == 0:
            return False
    return n > 1

def solve(s):
    for i in range(len(s)):
        if (isPrime(i) and not isPrime(int(s[i]))) or (not isPrime(i) and isPrime(int(s[i]))):
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t :
        s = input()
        print('YES' if solve(s) else 'NO')


        t -= 1