if __name__ == '__main__':
    t = int(input())
    while t:
        lst = []
        n = int(input())
        a = []
        b = []
        for _ in range(n):
            x, y = map(float, input().split())
            a += [x]
            b += [y]

        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if a[j] < a[i] and b[j] > b[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        print(max(dp))
        t -= 1
        
'''
3
2
1.0 1.0
1.5 0.0
3
1.0 1.0
1.0 1.0
1.0 1.0
6
1.5 9.0
2.0 2.0
2.5 6.0
3.0 5.0
4.0 2.0
10.0 5.5

'''