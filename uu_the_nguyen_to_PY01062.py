from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(s):
    cnt_prime = 0
    for x in s:
        if x == '2' or x == '3' or x == '5' or x == '7':
            cnt_prime += 1 
    return cnt_prime > len(s) - cnt_prime

if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        print('YES' if isPrime(len(s)) and check(s) else 'NO')
        t -= 1