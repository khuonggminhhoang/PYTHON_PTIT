if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    
    max_ = -10**9 -1
    min_ = 10**9 + 1
    for i in range(n):
        max_ = max(max_, max(a[i]))
        min_ = min(min_, min(a[i]))
    
    print(min_)
    for i in range(n):
        for j in range(m):
            if a[i][j] == min_:
                print(i + 1, j + 1)
            
    print(max_)
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_:
                print(i + 1, j + 1)
