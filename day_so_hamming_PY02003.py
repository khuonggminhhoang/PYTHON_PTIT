def list_hamming():
    i = 1
    while i <= 10 ** 18:
        j = 1
        while j <= 10 ** 18:
            k = 1
            while k <= 10 ** 18:
                arr_hamming.append(i * j * k)
                k *= 5
            j *= 3
        i *= 2
    arr_hamming.sort()

def binary_search(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r)//2
        if a[m] == x:
            return m + 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1

if __name__ == '__main__':
    t = int(input())
    arr_hamming = []
    list_hamming()
    while t:
        n = int(input())
        tmp = binary_search(arr_hamming, n)
        if tmp != -1:
            print(tmp)
        else:
            print('Not in sequence')
        t -= 1
    