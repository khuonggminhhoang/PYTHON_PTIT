if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))

    cnt = [-1] * 101
    for i in range(n):
        for j in range(n):
            if cnt[a[i][j]] == i - 1:
                cnt[a[i][j]] = i
    flag = False
    for x in a[0]:
        if cnt[x] == n - 1:
            print(x, end=' ')
            cnt[x] = -1
            flag = True
    if not flag :
        print('NOT FOUND' )
