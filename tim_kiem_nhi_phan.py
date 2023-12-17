def binary_search(a, l, r, x):
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
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    q = int(input())
    while q:
        x = int(input())
        print('YES' if binary_search(a, 0, n-1, x) else 'NO')
        q -= 1