from math import *

def isprime(s):
    s = int(s)
    for i in range(2, isqrt(s) + 1):
        if s % i == 0: 
            return False
    return s > 1

def sum_digit(s):
    a = [int(x) for x in s]
    return sum(a)

def prime_digit(s):
    for x in s:
        if x != '2' and x != '3' and x != '5' and x != '7':
            return False
    return True

if __name__ == '__main__':
    s = input()
    print('YES' if isprime(sum_digit(s)) and prime_digit(s) else 'NO')