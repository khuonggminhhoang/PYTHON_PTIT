def binarySearch(a, l, r, x):
    while l <= r:
        m = (l + r)//2
        if a[m] == x:
            return True
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return False

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    flag = False
    for i in range(n-1):
        if binarySearch(a, i + 1, n - 1, a[i] + k):
            flag = True
            break
    print(1 if flag else -1)