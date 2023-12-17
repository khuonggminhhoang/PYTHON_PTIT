from math import *

def als_prime(n):
    lst = []
    for i in range(2, isqrt(n) + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt != 0:
            lst.append([i, cnt])
    if n > 1: lst.append([n, 1])
    return lst

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        lst = als_prime(n)
        print('1 ', end='')
        for x in lst:
            print(f'* {x[0]}^{x[1]} ', end='')
        print()
        t -= 1