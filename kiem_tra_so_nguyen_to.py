import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

if __name__ =='__main__':
    n = int(input())
    print('YES' if isPrime(n) else "NO")