import math

def isPrime(n):
    if n == 1: 
        print(1)
        return
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: 
            print(i)
            return
    if n > 1: print(n)

if __name__ == '__main__':
    n = int(input())
    for i in range(n+1):
        isPrime(i)