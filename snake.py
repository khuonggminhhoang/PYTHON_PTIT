if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        if i % 2 == 0:
            print(*a[i])
        else:
            a[i] = a[i][::-1]
            print(*a[i])