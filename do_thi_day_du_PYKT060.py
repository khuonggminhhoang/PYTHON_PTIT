def DFS(u):
    global visited, adj, sub
    visited[u] = True
    sub += [u]
    for v in adj[u]:
        if not visited[v]:
            DFS(v)

def solve():
    global visited, sub
    for u in range(1, n + 1):
        if not visited[u]:
            sub = []
            DFS(u)
            if len(sub) > 1:
                for v in sub:
                    if len(adj[v]) != len(sub) - 1:
                        return 'NO'
    return 'YES'

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u] += [v]
        adj[v] += [u]

    visited = [False] * (n + 1)
    sub = []
    print(solve())

# Note: chỉ cần check xem các thành phần liên thông có đầy đủ hay không là được