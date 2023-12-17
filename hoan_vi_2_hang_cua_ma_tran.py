if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    r1, r2 = map(int, input().split())

    a[r1-1], a[r2-1] = a[r2-1], a[r1-1]
    
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
    