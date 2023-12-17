mod = 10**9 + 7
if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    sum = 0
    mul = 1
    for x in a:
        sum = ((sum%mod) + (x%mod)) % mod
        mul = ((mul%mod) * (x%mod)) % mod
    print(sum, mul, sep = '\n')