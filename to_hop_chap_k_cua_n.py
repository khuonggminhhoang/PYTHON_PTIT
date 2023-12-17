def fact(n):
    if n == 0: return 1
    return fact(n-1) * n

def tohop(n,k):
    return fact(n)//(fact(k) * fact(n-k))

if __name__ == '__main__':
    n, k = map(int, input().split())
    if k > n-k : 
        k = n-k
    print(tohop(n,k))
