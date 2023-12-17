def setup(n):
    global visited
    visited = [False] * (n + 1)

def DFS(u, v, n, tmpstr, res):
    global dct
    global visited
    visited[u] = True
    tmpstr += str(u) + ' '
    if u == v:
        res.append(tmpstr)
        return
    
    for i in dct[u]:
        if not visited[i]:
            DFS(i, v, n, tmpstr, res)  
            visited[i] = False

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, u, v = map(int, input().split())
        dct = {}
        for i in range(1, n + 1):
            dct[i] = []
        
        for _ in range(m):
            s, t = map(int, input().split())
            dct[s] += [t]

        visited = []
        setup(n)
        
        res = []
        DFS(u, v, n, '', res)

        lst = []
        for substr in res:
            tmp = list(map(int, substr.strip().split()))
            lst.append(set(tmp[1:-1]))
        
        tmp = lst[0].intersection(lst[1])
        for i in range(len(lst)):
            tmp = tmp.intersection(lst[i])
        print(len(tmp))
