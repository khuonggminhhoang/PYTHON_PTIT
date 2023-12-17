import math

def anlPrime(n):
    res = 0
    i = 2
    while i*i <= n:
        cnt = 0
        if n % i == 0 :
            res += 1
            if res > 3 : return 0
            while n%i == 0:
                n //= i
                cnt += 1
                if cnt > 1: return 0
        i += 1
    if n > 1: res += 1
    if res ==3 : return 1
    return 0

if __name__ == '__main__':
    n = int(input())
    print(anlPrime(n))