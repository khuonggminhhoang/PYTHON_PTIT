from math import *

def is_prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    dct = {}
    for x in a:
        dct[x] = 0
    lst = list(dct.keys())
    s = sum(lst)
    tmp = 0
    flag = True
    for i in range(len(lst)):
        tmp += lst[i]
        s -= lst[i]
        if is_prime(tmp) and is_prime(s):
            print(i)
            flag = False
            break
    if flag: print('NOT FOUND')

    