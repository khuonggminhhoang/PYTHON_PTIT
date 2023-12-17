def first_pos(a, x):
    ans = -1
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r)//2
        if a[m] == x:
            ans = m
            r = m - 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return ans

def last_pos(a, x):
    ans = -1
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r)//2
        if a[m] == x:
            ans = m
            l = m + 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return ans

def upper_bound(a, x):
    ans = -1
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r)//2
        if a[m] >= x:
            ans = m
            r = m - 1
        else:
            l = m + 1
    return ans

def lower_bound(a, x):
    ans = -1
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r)//2
        if a[m] > x:
            ans = m
            r = m - 1
        else:
            l = m + 1
    return ans

if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(first_pos(a,x))
    print(last_pos(a,x))
    print(upper_bound(a,x))
    print(lower_bound(a,x))
    print(last_pos(a,x) -first_pos(a,x))