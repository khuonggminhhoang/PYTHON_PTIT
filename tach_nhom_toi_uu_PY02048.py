if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n - 1):
        if a[i + 1] - a[i] > k:
            cnt += 1
    print(cnt + 1)