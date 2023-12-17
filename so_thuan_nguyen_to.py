import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

def checkDigit(n):
    sum = 0
    while n:
        r = n%10
        if r != 2 and r != 3 and r != 5 and r != 7:
            return False
        sum += r
        n //= 10
    return isPrime(sum)

if __name__ == '__main__':
    a, b = map(int, input().split())
    cnt = 0
    for n in range(a, b + 1):
        if checkDigit(n) and isPrime(n) :
            cnt+=1
    print(cnt)