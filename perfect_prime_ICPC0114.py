from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n%i == 0: return False
    return n > 1

def checkDigit(n):
    for x in n:
        if  x != '2' and x != '3' and x !='5' and x != '7':
            return False
    return True

def sumDigit(n):
    sum = 0
    for x in n:
        sum += int(x)
    return sum
 
def solve(n):
    return isPrime(int(n)) and isPrime(int(n[::-1])) and checkDigit(n) and isPrime(sumDigit(n))

if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = input()
        print('Yes' if solve(n) else 'No')
        t -= 1