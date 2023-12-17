if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    
    b = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            b[i][j] = a[j][i]
        b[i].sort()
    
    for i in range(n):
        for j in range(n):
            print(b[j][i], end=' ')
        print()
    