d = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]

def dfs(a, n, m, i, j):
    a[i][j] = 0
    for k in range(8):
        x = i + d[k][0]
        y = j + d[k][1]
        if 0 <= x < n and 0 <= y < m and a[x][y] == 1:
            dfs(a, n, m, x, y)

if __name__ == '__main__':
    n = int(input())
    s, t, u , v = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    dfs(a, n, n, s - 1, t - 1)
    print('YES' if a[u - 1][v - 1] == 0 else 'NO')

# 9
# 7 5 4 3
# 1 0 1 0 1 0 1 1 1
# 1 1 1 1 0 0 0 0 1
# 1 0 1 1 1 0 1 1 1
# 1 0 1 0 1 0 0 0 0
# 0 1 1 0 1 1 0 1 1
# 1 0 0 0 0 1 1 0 1
# 1 0 1 0 1 0 1 1 0
# 0 1 1 0 0 0 0 1 1
# 0 0 1 1 0 0 0 0 1