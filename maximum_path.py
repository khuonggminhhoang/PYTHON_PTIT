if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    dp = [[0 for _ in range(m)] for _ in range(n)]

    dp[0][0] = a[0][0]

    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + a[0][j]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + a[i][0]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + a[i][j]
            
    print(dp[n-1][m-1])