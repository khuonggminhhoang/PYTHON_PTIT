def fibo(n):
    f0 = 0
    f1 = 1
    fn = 0
    while True:
        if fn >= n:
            return fn
        fn = f0 + f1
        f0 = f1
        f1 = fn

if __name__ == '__main__':
    n = int(input())
    print(fibo(n))
