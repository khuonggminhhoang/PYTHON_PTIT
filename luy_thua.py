mod = 1000000007
def binPow(a,b):
    if b == 0: return 1
    r = binPow(a,b//2)
    if b%2 == 1:
        return ((r%mod) * (r%mod))%mod * a %mod
    else :
        return ((r%mod) * (r%mod)) % mod

if __name__ == '__main__':
    a,b = map(int, input().split())
    print(binPow(a,b))