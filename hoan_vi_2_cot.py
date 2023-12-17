if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    c1, c2 = map(int, input().split())
    c1, c2 = c1 - 1, c2 - 1
    for i in range(n):
        a[i][c1], a[i][c2] = a[i][c2], a[i][c1]
    
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()