if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    tmp = 1  # đếm số phần tử khác nhau trong list
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            tmp += 1
    min = a[0]
    max = a[n-1]
    print(max - min - tmp + 1)