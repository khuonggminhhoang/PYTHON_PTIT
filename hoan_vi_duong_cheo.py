def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))

    for i in range(n):
        # swap(a[i], i, n - i - 1)
        a[i][i], a[i][n - i - 1] = a[i][n - i - 1], a[i][i]
    
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()

    