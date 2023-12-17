from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

def palin(n):
    tmp = n
    rev = 0
    while tmp != 0:
        rev = 10 * rev + tmp % 10
        tmp //= 10
    return n == rev

def sqrNum(n):
    return sqrt(n) == isqrt(n)

def sumDigit(n):
    res = 0
    while n != 0:
        res += n%10
        n //= 10
    return res

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
    for x in a:
        if isPrime(x): cnt1 += 1
        if palin(x) : cnt2 += 1
        if sqrNum(x) : cnt3 += 1
        if isPrime(sumDigit(x)) : cnt4 += 1
    print(cnt1, cnt2, cnt3, cnt4, sep='\n')