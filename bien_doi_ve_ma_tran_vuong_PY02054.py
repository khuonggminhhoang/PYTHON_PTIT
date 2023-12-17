def solve(a, n, m):
    ans = []
    if n > m:
        cnt = n - m
        for i in range(n):
            if i % 2 == 0 and cnt > 0:
                cnt -= 1
            else:
                ans.append(a[i])
    elif n < m:
        for i in range(n):
            cnt = m - n
            arr = []
            for j in range(m):
                if j % 2 == 1 and cnt > 0:
                    cnt -= 1
                else:
                    arr += [a[i][j]]
            ans.append(arr)   
    else:
        ans = a
    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    lst = solve(a, n, m)
    for i in range(len(lst)):
        print(*lst[i])