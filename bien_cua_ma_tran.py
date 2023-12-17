if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if i == n-1 or i == 0 or j == 0 or j == n - 1:
                print(a[i][j], end=' ')
        