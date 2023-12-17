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
    a = [1, 2, 2, 3, 5, 10]
    print(binary_search(a, 0, len(a)-1, 5))