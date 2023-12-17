if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 0
    idx = 0
    for i in range(n):
        if a[i] > b[idx]:
            ans += 1
            idx += 1
    print(ans)