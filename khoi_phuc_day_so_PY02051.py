#idea: if b[i] ==2 thì các =1+1 do nguyên dương
#tìm đc công thức: tổng dòng 1 = (n-2)*a[0] + sum(a)
#tổng các số bên phải dg chéo chính = (n-1)*(sum(a)) = 1/2.sum_b => tìm đc a[0] =>...

if __name__ == '__main__':
    n = int(input())
    b = [0] * n
    a = [0] * n
    sum_b = 0
    sum_row_1 = 0
    for i in range(n):
        b[i] = list(map(int, input().split()))
        sum_b += sum(b[i])
        if i == 0:
            sum_row_1 = sum(b[i])
    if n == 2:  
        print(f'1 {b[0][1] - 1}')
    else:
        sum_a = int(1/2 * sum_b * 1/(n-1))
        a[0] = (sum_row_1 - sum_a)//(n-2)
        for i in range(1, n):
            a[i] = b[0][i] - a[0]
        print(*a)
    
    