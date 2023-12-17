from math import *

def sev():
    prime[0] = prime[1] = False
    for i in range(2, isqrt(10**6 + 1) + 1):
        if prime[i] :
            for j in range(i*i, 10**6 + 1, i):
                prime[j] = False

if __name__ == '__main__':
    prime = [True] * (10**6 + 1)
    t = int(input())
    sev()
    while t:
        n = int(input())
        ans = 0
        for i in range(n+1):
            if prime[i] and prime[i - 6] and (prime[i - 2] or prime[i - 4]):
                ans += 1
        print(ans)
        t-= 1