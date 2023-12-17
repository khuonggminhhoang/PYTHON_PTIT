def upper(a, l, r, x):
    ans = -1
    while l <= r:
        m = (l + r)//2
        if a[m] > x:
            ans = m
            r = m - 1
        else:
            l = m + 1
    return ans

if __name__== '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n - 1):
        tmp = upper(a, i + 1, n - 1, k - a[i])
        if tmp != -1:
            ans += (n-tmp)
    print(ans)