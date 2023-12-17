from math import *

default = 10001
prime = [True] * default

def seive():
    prime[0] = prime[1] = False
    for i in range(2, isqrt(default) + 1):
        if prime[i]:
            for j in range(i*i, default, i):
                prime[j] = False

    lst = []
    for i in range(default):
        if prime[i]:
            lst += [i]
    return lst

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    arr = seive()
    ans = 0
    for x in a:
        tmp = int(1e9)
        for y in arr:
            tmp = min(tmp, abs(x - y))
        ans = max(ans, tmp)
    print(ans)