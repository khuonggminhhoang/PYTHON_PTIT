if __name__ == '__main__':
    n = int(input())
    a = []
    while True:
        tmp = list(map(int, input().split()))
        a += tmp
        if len(a) == n: break

    b = [0] * n
    odd = []
    even = []
    for i in range(n):
        if a[i] % 2 != 0:
            b[i] = 1
            odd.append(a[i])
        else:
            even.append(a[i])
    
    odd.sort(key= lambda x : -x)
    even.sort()
    idx_odd = 0
    idx_even = 0
    ans = []
    for i in range(n):
        if b[i] == 1:
            ans.append(odd[idx_odd])
            idx_odd += 1
        else:
            ans.append(even[idx_even])
            idx_even += 1
    
    print(*ans)