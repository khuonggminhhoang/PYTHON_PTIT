from math import *

def lower(a, l, r, x):
    ans = -1
    while l <= r:
        m = (l + r)//2
        if a[m] <= x:
            ans = m
            l = m + 1
        else:
            r = m - 1
    return ans

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    l, r = 0, n-1
    while l <= r:
        if a[l] + a[r] <= k:
            ans += 1
            l += 1
            r -= 1
        else:
            ans += 1
            r -= 1
    print(ans)