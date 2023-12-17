if __name__ == '__main__':
    a,k,n = map(int, input().split())
    first = ((a+k-1)//k) *k - a
    last = ((n)//k) *k - a
    if last - first < k:
        print(-1)
    else:
        for x in range(first, last + 1, k):
            print(x, end = ' ')