def Try(i, arr):
    global n, k
    if len(arr) == k:
        for i in arr:
            print(a[i-1], end=' ')
        print()
        return
    for j in range(i + 1, n + 1):
        Try(j, arr + [j])

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(set(map(int, input().split())))
    a.sort()
    n = len(a)
    Try(0,[])
