if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a[1:] = sorted(a[1:], reverse= True)
    ans = sum(a[0:k + 1])
    for i in range(k + 1, n):
        ans -= a[i]
    print(ans)
    