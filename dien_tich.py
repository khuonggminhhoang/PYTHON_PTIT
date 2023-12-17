d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cnt = 0
n, m = 0, 0
a = [0] * 501

def dfs(i, j):
    global cnt
    a[i][j] = 0
    cnt += 1
    for k in range(4):
        x = i + d[k][0]
        y = j + d[k][1]
        if 0 <= x < n and 0 <= y < m and a[x][y] == 1:
            dfs(x, y)

if __name__ == '__main__':
    ans = -10**9 - 1
    n, m = map(int, input().split())
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            cnt = 0
            if a[i][j] == 1:
                dfs(i, j)
                ans = max(ans, cnt)
    
    print(ans)

# 5 6
# 0 1 0 1 0 1
# 0 0 0 1 1 0
# 0 1 1 0 1 1
# 0 1 1 0 0 0
# 0 0 0 0 0 0