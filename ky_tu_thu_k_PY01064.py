def mul(k):
    if k == 0 : return 1
    p = mul(k//2)
    if k%2 == 1: return 2 * p * p
    return p * p

def search(n, k):
    mid = mul(n - 1) - 1
    while k != mid:
        if k > mid:
            k = k - mid - 1
        n -= 1
        mid //= 2
    return chr(ord('@') + n)

if __name__ == '__main__':
    t = int(input())
    while t:
        n, k = map(int, input().split())
        print(search(n, k-1))
        t -= 1