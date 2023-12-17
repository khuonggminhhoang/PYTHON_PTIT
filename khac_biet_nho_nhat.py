if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    res = 10**18
    for i in range(n-1):
        if (a[i+1] - a[i] < res):
            res = a[i+1] - a[i]
    print(res)