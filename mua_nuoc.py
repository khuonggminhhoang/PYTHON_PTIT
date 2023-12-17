if __name__ == '__main__':
    n, a, b = map(int, input().split())
    if a <= b/2:
        print(n*a)
    elif n%2 == 0:
        print(n//2 * b)
    else:
        print(n//2 * b + a)
