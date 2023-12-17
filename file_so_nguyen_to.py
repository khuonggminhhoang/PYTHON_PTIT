from math import *

def is_prime(num):
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    return num > 1

if __name__ == '__main__':
    inp = open('input.txt', 'rt')
    out = open('output.txt', 'wt')
    s = inp.read()
    lst = list(map(int, s.split()))
    a = []
    for x in lst:
        if is_prime(x):
            a.append(x)
    a.sort()
    for x in a:
        out.write(str(x) + ' ')