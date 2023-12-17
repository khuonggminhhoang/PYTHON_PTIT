def mul_matrix(a, kernel, n, m):
    ans = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            for row in range(i-1, i + 2):
                for col in range(j-1, j + 2):
                    ans += a[row][col] * kernel[1-(i - row)][1 - (j - col)]
    return ans

if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int ,input().split())
        a = [0] * n
        for i in range(n):
            a[i] = list(map(int, input().split()))
        
        kernel = [0] * 3
        for i in range(3):
            kernel[i] = list(map(int, input().split()))
        print(mul_matrix(a, kernel, n, m))

