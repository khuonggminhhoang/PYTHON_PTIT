def palin(n):
    s = str(n)
    return s == s[::-1]


if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        for j in range(0, i + 1):
            if palin(a[i][j]) :
                ans +=1
    print(ans)
