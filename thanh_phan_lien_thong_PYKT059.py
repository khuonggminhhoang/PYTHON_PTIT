def DFS(u):
    global visited, dct
    visited[u] = True
    for v in dct[u]:
        if not visited[v]:
            DFS(v)

if __name__ == '__main__':
    n, m, e = map(int, input().split())
    dct = {}
    visited = [False] * (n + 1) 
    for i in range(1, n + 1):
        dct[i] = []
    for _ in range(m):
        u, v = map(int, input().split())
        dct[u] += [v]
        dct[v] += [u]

    DFS(e)
    for i in range(1, n + 1):
        if not visited[i]:
            print(i)
    
        