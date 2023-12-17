from math import *

prime = [True] * (10**6 + 1)
F = [0] *(10**6 + 1)

def sieve():
    prime[0] = prime[1] = False
    for i in range(2, isqrt(10**6 + 1) + 1):
        if prime[i]:
            for j in range(i*i, 10**6 + 1, i):
                prime[j] = False

def solve():
    F[0] = F[1] = 0
    F[2] = 2
    for i in range(3, 10 ** 6 + 1):
        if prime[i]:
            F[i] = F[i-1] * i
        else:
            F[i] = F[i-1]
        F[i] %= (10**9 + 7)

if __name__ == '__main__':
    sieve()
    solve()
    t= int(input())
    while t != 0:
        n = int(input()) 
        print(F[n])
        t-=1