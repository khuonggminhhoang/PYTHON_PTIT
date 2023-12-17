if __name__ == '__main__':
    n = int(input())
    a = [[0 for _ in range(n)] for _ in range(n)]
    id = 1
    l = 0
    while l <= n//2:
        for j in range(l, n - l - 1):
            a[l][j] = id 
            id += 1
        for i in range(l, n - l - 1):
            a[i][n - l - 1] = id
            id += 1
        for j in range(n - l - 1, l , -1):
            a[n - l - 1][j] = id
            id += 1
        for i in range(n - l - 1, l , -1):
            a[i][l] = id
            id += 1
        l += 1
    if n % 2 == 1:
        a[n//2][n//2] = id
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()