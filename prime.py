from math import *

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i ==  0: return False
    return n > 1
        
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    
    for x in a:
        if isPrime(x):
            print(x, end=' ')
        
