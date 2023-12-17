import math

if __name__ == '__main__':
    t = int(input())
    while t:
        a = int(input())
        b = int(input())
        print(math.gcd(a,b))
        t -= 1