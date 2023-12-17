import math

def check(n):
    if n%10 != 6 and n%10 != 8:
        return False
    i = 2
    while True:
        tmp = 2**(i-1) * (2**i - 1)
        if tmp == n : return True
        if tmp > n : return False
        i+=1


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n%i == 0 :
            return False
    return n > 1

def perfectNumber(n):
    for i in range(2, 33):
        if isPrime(i) and isPrime(2**i - 1):
            pftnum = (2 ** i - 1) * (2 ** (i-1))
            if pftnum == n:
                return True
    return False

if __name__ == '__main__':
    n = int(input())
    print('YES' if perfectNumber(n) else 'NO')