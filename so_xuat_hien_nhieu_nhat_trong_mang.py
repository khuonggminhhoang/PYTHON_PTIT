if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    cnt = 1
    res = a[0]
    for i in range(1, n):
        if a[i] == a[i-1]:
            cnt += 1
        else:
            if cnt > ans:
                ans = cnt
                res = a[i-1]
            cnt = 1
    print(res, ans)