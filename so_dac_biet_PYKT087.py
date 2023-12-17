mod = int(1e9) + 7

def solve(n, k):
    ans = 0
    tmp = 1
    while k != 0:
        if k % 2 == 1:
            ans += tmp
            ans %= mod
        k //= 2
        tmp *= n
        tmp %= mod
    return ans

if __name__ == '__main__':
    t = int(input())
    while t:
        n, k = map(int, input().split())
        print(solve(n,k))
        t -= 1
