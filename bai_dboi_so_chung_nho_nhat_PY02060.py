from math import *

mod = 1000000007

if __name__ == '__main__':
    t = int(input())
    while t :
        a, b = map(int, input().split())
        mul = 1
        for i in range(a, b+1):
            mul *= i
            mul %= mod

        divisor = set()
        for i in range(1, isqrt(mul) + 1):
            if mul % i == 0:
                divisor.add(i)
                divisor.add(mul//i)
        divisor = sorted(divisor)
        ans = 0
        for i in range(len(divisor) - 1):
            for j in range(i + 1, len(divisor)):
                if lcm(divisor[i], divisor[j]) == mul:
                    print(divisor[i],divisor[j])
                    ans += 1
                    ans %= mod
        ans = (ans * 2) % mod
        ans = (ans + 1) % mod
        print(ans)
        t -= 1