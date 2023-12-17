#Note: sử dụng prefix sum trên ma trận : pre[i][j] là giá trị tổng các phần tử của khối 0 -> i, 0 -> j
#link tham khảo : https://www.youtube.com/watch?v=KxQkpu842rc

if __name__ == '__main__':
    t = int(input())
    while t:
        n, m, l = map(int, input().split())
        arr = [0] * (n + 1)

        arr[0] = [0] * (n + 1)  # set các phần tử của hàng 0 của arr bằng 0
        for i in range(1, n + 1):
            arr[i] = [0]  + list(map(int, input().split()))

        pre = [[0 for _ in range(m +1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                pre[i][j] = pre[i][j - 1] + pre[i - 1][j] - pre[i - 1][j - 1] + arr[i][j]
                # pre[i][j] là giá trị tổng các phần tử của khối 0 -> i, 0 -> j

        row = n - l + 1
        col = m - l + 1
        ans = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                h1 = i + 1
                h2 = i + l 
                c1 = j + 1
                c2 = j + l 
                ans[i][j] = pre[h2][c2] - pre[h1 - 1][c2] - pre[h2][c1 - 1] + pre[h1 - 1][c1 - 1]
                # ans[i][j] lưu tổng của khối từ c1 -> c2, h1 -> h2
                ans[i][j] //= l**2

        for x in ans:
            print(*x)

        t -= 1