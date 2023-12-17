d = [[1, 0] ,[0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1],[1, -1], [1, 1]]

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(m):
            flag = True
            for k in range(8):
                x = i + d[k][0]
                y = j + d[k][1]
                if 0 <= x < n and 0 <= y < m and a[i][j] <= a[x][y]:
                    flag = False 
                    break
            if flag:
                cnt += 1
    print(cnt)