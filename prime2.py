from math import *

prime = [True] * (10**6 + 1)
F = [0] * (10**6 + 1)

def sieve():
    prime[0] = prime[1] = False
    for i in range(2, isqrt(10**6 + 1) + 1):
        if prime[i]:
            for j in range(i*i, 10**6 + 1,i):
                prime[j] = False

def solve():
    for i in range(1, 10** 6 + 1):
        if prime[i]:
            F[i] = F[i-1] + 1
        else:
            F[i] = F[i-1]

if __name__ == '__main__':
    sieve()
    solve()
    t = int(input())
    while t != 0:
        l, r = map(int,input().split())
        if l == 0:
            print(F[r])
        else:
            print(F[r] - F[l-1])
        t -= 1