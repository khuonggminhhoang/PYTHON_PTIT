from math import *

def mul_divisor(n):
    ans = 0
    for i in range(2, isqrt(n)+ 1):
        mul = 1
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt != 0:
            mul *= cnt * i
            ans += mul
    if n > 1: ans += n
    return ans

if __name__ == '__main__':
    t = int(input())
    tmp = [0]* ( 1001)
    for i in range(1001):
        tmp[i] = mul_divisor(i)
    sum = 0
    while t:
        n = int(input())
        sum += tmp[n]
        t -= 1
    print(sum)