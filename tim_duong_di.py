d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dfs(arr, n, m, i, j):
    arr[i][j] = 0
    for k in range(4):
        x = i + d[k][0]
        y = j + d[k][1]
        if 0 <= x < n and 0 <= y < m and a[x][y] == 1:
            dfs(arr, n, m, x, y)

if __name__ == '__main__':
    n, m = map(int, input().split())
    s, t, u, v = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    dfs(a, n, m, s - 1, t - 1)
    print('YES' if a[u-1][v-1] == 0 else 'NO')
    
