import math

def round_(n):
    if n <= 9: return n

    i = 10
    while n > i:
        r = n%i
        tmp = n/i
        if r >= 5 * (i//10):
            tmp = math.ceil(tmp)
        else:
            tmp = math.floor(tmp)
        n = tmp * i
        i *= 10
    return n

"""
n = 1234 r = 4 tmp = 123 i = 10
n = 1230 r = 30 tmp = 12 i = 100
n = 1200 r = 200 tmp = 1 i =1000
n = 1000 i = 10000

"""

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        print(round_(n))
        t -= 1






















