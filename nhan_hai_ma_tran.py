if __name__ == '__main__':
    n, m, p = map(int, input().split())
    a = [0] * n
    b = [0] * m
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(m):
        b[i] = list(map(int, input().split()))
    
    arr = [[0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                arr[i][j] += a[i][k] * b[k][j]
        
    for i in range(n):
        for j in range(p):
            print(arr[i][j], end=' ')
        print()