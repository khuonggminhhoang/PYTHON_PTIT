if __name__ == '__main__':
    n, m = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    idx1, idx2 = 0, 0
    ans = []
    while(idx1 < n) and (idx2 < m):
        if b[idx1] <= c[idx2]:
            ans.append('b' + str(idx1 + 1))
            idx1 += 1
        else:
            ans.append('c' + str(idx2 + 1))
            idx2 += 1
    
    while idx1 < n:
        ans.append('b' + str(idx1 + 1))
        idx1 += 1
    
    while idx2 < m:
        ans.append('c' + str(idx2 + 1))
        idx2 += 1
    
    for x in ans:
        print(x, end=' ')