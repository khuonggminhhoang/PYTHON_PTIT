from math import *

def palin(s):
    a = s[::-1]
    return a == s

def sieve():
    emirp[0] = emirp[1] = False
    for i in range(2, isqrt(10**6 + 1) + 1):
        if emirp[i]:
            for j in range(i*i, 10**6 + 1, i):
                emirp[j] = False
        if palin(str(i)): emirp[i] = False

def solve(arr, n):
    for i in range(n):
        tmp = int(str(i)[::-1])
        if tmp > i and tmp < n and arr[i] and arr[tmp]:
            print(i, tmp, end=' ')


if __name__ == '__main__':
    emirp = [True] * (10**6+1)
    sieve()
    t = int(input())
    while t != 0 :
        n = int(input())
        solve(emirp, n)
        print()
        t -= 1