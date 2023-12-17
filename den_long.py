if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = -1
    for i in range(n - 1):
        ans = max(ans, a[i+1] - a[i])
    ans = max(ans/2, a[0]/2, (k - a[-1])/2)
    print('%.10f' %ans)