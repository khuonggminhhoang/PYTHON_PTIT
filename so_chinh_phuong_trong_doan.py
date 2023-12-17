import math

if __name__ == '__main__':
    a,b = map(int, input().split())
    for i in range(math.ceil(math.sqrt(a)), math.isqrt(b) + 1):
        print(i*i, end = ' ')