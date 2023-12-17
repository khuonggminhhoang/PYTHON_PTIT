if __name__ == '__main__':
    n = int(input())
    a = [0]*n
    for i in range(n):
        a[i] = list(input())
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[i][j] == 'C':
                cnt += 1 
        ans += cnt * (cnt - 1)//2

    for j in range(n):
        cnt = 0
        for i in range(n):
            if a[i][j] == 'C':
                cnt += 1
        ans += cnt * (cnt - 1)//2
    print(ans)