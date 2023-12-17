import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n%i == 0:
            return False
    return n>1

def sumDigit(n):
    sum = 0
    while n!=0:
        sum += n%10
        n //= 10
    return sum

def gcd(a,b):
    while b!= 0:
        tmp = a%b
        a=b
        b=tmp
    return a

if __name__ == '__main__':
    t = int(input())
    while t:
        a, b = map(int, input().split())
        gcd = math.gcd(a,b)
        print('YES' if isPrime(sumDigit(gcd)) else 'NO')
        t -= 1

