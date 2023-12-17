from math import *

prime = [True] * 1000001

def seive():
    prime[0] = prime[1] = False
    for i in range(2, isqrt(1000001) + 1):
        if prime[i]:
            for j in range(i*i, 1000001, i):
                prime[j] = False


if __name__ == '__main__':
    seive()
    n = int(input())
    a = [int(x) for x in input().split()]
    cnt = [0] * 1000001
    for x in a:
        if prime[x]:
            cnt[x] += 1
        
    for x in a:
        if cnt[x] != 0:
            print(x, cnt[x])
            cnt[x] = 0