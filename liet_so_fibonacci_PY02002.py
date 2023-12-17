if __name__ == '__main__':
    t = int(input())
    f = [0] * 93
    f[0] = 0
    f[1] = 1
    for i in range(2, 93):
        f[i] = f[i-1] + f[i-2]
    while t:
        a,b = map(int, input().split())
        for i in range(a,b + 1):
            print(f[i], end=' ')
        print()
        t-=1