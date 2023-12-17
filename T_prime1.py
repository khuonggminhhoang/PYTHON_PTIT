import math

def isPrime(n):
    for i in range(2, math.isqrt(n)+1):
        if n%i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    cnt = 0
    n = int(input())
    for i in range(2, math.isqrt(n)+1):
        if isPrime(i):
            cnt+=1
            print(i**2, end=' ')
    print(cnt)