def fibo(n):
    if n == 1 or n == 2: return n-1
    f1 = 0
    f2 = 1
    for i in range(3,n+1):
        fn = (f1%1000000007 + f2%1000000007) % 1000000007
        f1 = f2
        f2 = fn
    return fn

if __name__ == '__main__':
    n = int(input())
    print(fibo(n))