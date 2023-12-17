from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n %i == 0:
            return False
    return n > 1

def sum_digit(s):
    sum = 0
    for x in s:
        sum += int(x)
    return sum

def is_pos_even(s):
    for i in range(0,len(s), 2):
        if int(s[i]) % 2 != 0:
            return False
    return True

def is_pos_odd(s):
    for i in range(1, len(s), 2):
        if int(s[i]) % 2 == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        print('YES' if (isPrime(sum_digit(s)) and is_pos_even(s) and is_pos_odd(s)) else 'NO')
        t -= 1