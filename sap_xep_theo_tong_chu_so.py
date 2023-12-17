from functools import *

def sum_digit(n):
    sum = 0
    while n != 0:
        sum += n%10
        n //= 10
    return sum

def cmp(a, b):
    if sum_digit(a) != sum_digit(b):
        return sum_digit(a) - sum_digit(b)
    else:
        return a - b

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    # a.sort(key= cmp_to_key(cmp))
    a.sort(key = lambda x : (sum_digit(x), x))
    for x in a :
        print(x, end=' ')