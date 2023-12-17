from math import *

def first_pos(a, l, r, x):
    ans = -1
    while l <= r:
        m = (l +r)//2
        if a[m] == x:
            ans = m
            r = m - 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return ans

def last_pos(a, l, r, x):
    ans = -1
    while l <= r:
        m = (l +r)//2
        if a[m] == x:
            ans = m
            l = m + 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return ans

if __name__ == '__main__':
    n, k = map(int,input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(0, n - 1):
        cnt += last_pos(a,i + 1, n-1, k - a[i]) - first_pos(a, i + 1, n - 1, k - a[i]) + 1
    print(cnt)