d = [[1, 0] ,[0, 1], [-1, 0], [0, -1]]

def DFS(a, n, m, i, j):
    a[i][j] = 0
    for k in range(4):
        x = i + d[k][0]
        y = j + d[k][1]
        if 0 <= x < n and 0 <= y < m and a[x][y] == 1:
            DFS(a, n, m, x, y)



if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j]:
                DFS(a, n, m, i, j)
                cnt += 1
    print(cnt)