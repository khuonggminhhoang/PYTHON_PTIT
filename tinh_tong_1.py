def Sum(n):
    if n == 1: return 1
    return Sum(n-1) + n

if __name__ == '__main__':
    n = int(input())
    print(Sum(n))