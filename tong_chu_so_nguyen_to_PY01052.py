from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n %i == 0:
            return False
    return n > 1

def sum_digit(s):
    sum = 0
    for x in s:
        sum += int(x)
    return sum

if __name__ == '__main__':
    t= int(input())
    while t :
        s = input()
        print('YES' if isPrime(sum_digit(s)) else 'NO')
        t -= 1