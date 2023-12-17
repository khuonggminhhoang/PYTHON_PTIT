import math

if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n, x, m = map(float, input().split())
        print(math.ceil((math.log(m/n) / math.log(1 + x/100))))
        t -= 1