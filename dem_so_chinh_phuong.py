import math

if __name__ == '__main__':
    a, b = map(int, input().split())
    a = math.ceil(math.sqrt(a))
    b = math.isqrt(b)
    print((b-a) + 1)
