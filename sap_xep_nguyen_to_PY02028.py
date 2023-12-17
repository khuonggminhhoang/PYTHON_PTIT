from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = [0 for _ in range(n)]
    lst_prime = []
    for i in range(n):
        if isPrime(a[i]):
            b[i] = 1
            lst_prime += [a[i]]

    lst_prime.sort()
    ind = 0
    for i in range(n):
        if b[i] == 0:
            print(a[i], end=' ')
        else:
            print(lst_prime[ind], end=' ')
            ind += 1