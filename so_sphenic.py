import math

def anlPrime(n):
    res = 0
    for i in range(2,math.isqrt(n)+1):
        cnt = 0
        if n % i == 0 :
            while n%i == 0:
                n //= i
                cnt += 1
            if cnt >= 2 : return 0
            if cnt == 1 : res += 1
    if n != 1: res += 1
    if res ==3 : return 1
    return 0

if __name__ == '__main__':
    n = int(input())
    print(anlPrime(n))