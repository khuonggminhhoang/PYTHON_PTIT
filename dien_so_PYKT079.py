if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        tmp = 1
        for i in range(n-1):
            if a[i] != a[i + 1]:
                tmp += 1
        maxx = a[n-1]
        minx = a[0]
        print(maxx - minx - tmp + 1)
        t-= 1