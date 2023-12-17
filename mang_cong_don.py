if __name__ == '__main__':
    n =int(input())
    a = list(map(int, input().split()))
    f = [0]* n
    f[0] = a[0]
    for i in range(1, n):
        f[i] = f[i-1] + a[i]
    for x in f:
        print(x, end=' ') 