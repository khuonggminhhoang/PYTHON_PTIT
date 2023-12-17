if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        ins, dele, cop = map(int, input().split())
        dp = [0] * (n + 1)
        dp[1] = ins
        for i in range(2, n + 1):
            if i % 2 == 0:
                dp[i] = min(dp[i - 1] + ins, dp[i//2] + cop)
            else:
                dp[i] = min(dp[i - 1] + ins, dp[i//2 + 1] + cop + dele)
        print(dp[n])
        
        t -= 1