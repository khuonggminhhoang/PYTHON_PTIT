def binPow(a,b):
    a %= 10
    res = 1
    while b!=0:
        if b%2 == 1:
            res *= a
            res %= 10
        a *= a
        a %= 10
        b //= 2
    return res

if __name__ == '__main__':
    a,b = map(int, input().split())
    print(binPow(a,b))