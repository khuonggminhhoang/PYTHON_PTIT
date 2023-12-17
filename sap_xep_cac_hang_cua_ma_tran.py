if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
        a[i] = sorted(a[i])
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
