from math import *

# số lượng ước số của n
def number_of_divisor(n):
    ans = 1
    for i in range(2, isqrt(n) + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1 
            n //= i
        ans *= (cnt + 1)
    if n > 1:
        ans *= (1 + 1) 
    return ans

def sieve():
    anti_prime[1] = anti_prime[2] = anti_prime[4] = anti_prime[6] = anti_prime[12] = anti_prime[24] = True 
    max_divisor = 8
    for i in range(25, 100):
        tmp = number_of_divisor(i)
        if tmp > max_divisor:
            anti_prime[i] = True
            max_divisor = tmp
    for i in range(1, 100):
        if anti_prime[i]:
            print(i, end=' ')


if __name__ == '__main__':
    t = int(input())
    anti_prime = [False] * (100)
    sieve()
    while t:
        n = int(input())
        print(number_of_divisor(n))
        t -= 1