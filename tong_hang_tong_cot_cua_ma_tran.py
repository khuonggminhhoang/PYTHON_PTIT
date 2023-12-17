if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    
    for i in range(n):
        s = sum(a[i])
        print(s, end=' ')
    print()

    for j in range(m):
        s = 0
        for i in range(n):
            s += a[i][j]
        print(s, end=' ')
