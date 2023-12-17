if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    sum_matrix = 0
    for i in range(n):
        a[i] = list(map(int, input().split()))
        sum_matrix += sum(a[i]) - a[i][i]
    
    sum_up = sum_down = 0
    for i in range(n):
        for j in range(i + 1, n):
            sum_up += a[i][j]
    sum_down = sum_matrix - sum_up

    k = int(input())
    if abs(sum_up - sum_down) > k:
        print('NO')
    else:
        print('YES')
    print(abs(sum_up - sum_down))
