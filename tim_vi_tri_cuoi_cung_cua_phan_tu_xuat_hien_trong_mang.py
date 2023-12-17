def first_pos(a, l, r, x):
    ans = -1
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

# tìm vị tri phần tử xuất hiện đầu tiên có giá trị >= X trong mảng đã sắp xếp tăng dần
def upper_bound(a, l, r, x):
    ans = -1
    while l <= r:
        m = (l + r)//2
        if a[m] >= x:
            ans = m
            r = m - 1
        else:
            l = m + 1 
    return ans

# tìm vị tri phần tử xuất hiện đầu tiên có giá trị > X trong mảng đã sắp xếp tăng dần
def lower_bound(a, l, r, x):
    ans = -1
    while l <= r:
        m = (l + r)//2
        if a[m] > x:
            ans = m
            r = m - 1
        else:
            l = m + 1 
    return ans

if __name__ == '__main__':
    a = [1,1,2,2,4,5,7,7,10]
    print(first_pos(a, 0, len(a) - 1, 7))
    # O(long(N))
    print(upper_bound(a, 0, len(a)-1, 4.2))
    print(lower_bound(a, 0, len(a)-1, 7.1))