def binPow(a, b):
    res = 1
    while b!=0:
        if b%2 == 1:
            res *= a
        b //= 2
        a *= a
    return res

if __name__ == '__main__':
    a,b = map(int, input().split())
    print(binPow(a,b))