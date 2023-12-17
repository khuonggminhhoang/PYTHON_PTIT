# sinh tổ hợp bằng quay lui
def Try(start, path):
    if len(path) == k:
        res.append(path[:])
        return
    
    for i in range(start, n + 1):
        path.append(i)
        Try(i + 1, path)
        path.pop()

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input().split()
    st = set(s)
    lst = list(st)
    lst.sort()
    n = len(lst)
    res = []
    Try(1, [])
    
    
    
    for sub_lst in res:
        for x in sub_lst:
            print(lst[x - 1], end=' ')
        print()
