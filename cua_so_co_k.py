if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # cach 1 :
    ans = 0
    for i in range(n):
        if i < k:
            ans += a[i]
        else:
            print(ans, end=' ')
            ans = ans - a[i - k] + a[i]
    print(ans)