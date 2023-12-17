import math

def solve(n):
    ans = 0
    for i in range(2, math.isqrt(n) + 1):
        if n%i == 0:
            while n%i ==0 :
                n //= i
                ans = i
    if n > 1 :
        ans = n
    return ans

if __name__ == '__main__':
    t = int(input())
    while t :
        n = int(input())
        print(solve(n))
        t-=1