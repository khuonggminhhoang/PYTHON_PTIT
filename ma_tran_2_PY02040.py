if __name__ == '__main__':
    n = int(input())
    arr = [0] * n
    for i in range(n):
        arr[i] = list(map(int, input().split()))
    k = int(input())
    sum_top , sum_bottom = 0, 0
    for i in range(n):
        for j in range(n-i-1):
            sum_top += arr[i][j]

    for i in range(n):
        for j in range(n - i, n):
            sum_bottom += arr[i][j]

    ans = abs(sum_top - sum_bottom)
    print('YES' if ans <= k else 'NO')
    print(ans)
