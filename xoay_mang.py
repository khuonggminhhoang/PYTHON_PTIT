if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n, d = map(int, input().split())
        a = list(map(int, input().split()))
        ans = a[d:] + a[:d]
        for x in ans:
            print(x, end=' ')
        print()
        t -= 1