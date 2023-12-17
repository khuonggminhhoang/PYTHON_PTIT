import math

def anlPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            cnt = 0
            while n%i == 0:
                cnt += 1
                n //= i
            if cnt > 1: return True
    return False

if __name__ == '__main__':
    a,b = map(int, input().split())
    for i in range(a, b+1):
        if anlPrime(i):
            print(i, end=' ')