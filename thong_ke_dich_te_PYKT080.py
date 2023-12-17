def solve(i, j):
    ans = 0
    for idx in range(8):
        x = i + d[idx][0]
        y = j + d[idx][1]
        if x >= 0 and y >= 0 and x < m and y < n:
            ans += a[x][y]
            a[x][y] = 0
    return ans

if __name__ == '__main__':
    d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    
    m, n = map(int, input().split())
    a = [0] * m
    save = []
    for i in range(m):
        a[i] = list(map(int, input().split()))
        for j in range(n):
            if a[i][j] == -1:
                save.append([i, j])
    
    res = 0
    while len(save):
        i, j = save.pop(0)
        res += solve(i,j)
    print(res)