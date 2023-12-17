import math

def stn(n):
    tmp = n
    sum = 0
    while tmp :
        sum = sum * 10 + tmp%10
        tmp //= 10
    return n == sum

def check(n):
    if stn(n) == False: return False
    res = 0  #dem uoc nguyen to
    for i in range(2, math.isqrt(n) + 1):
        if n%i == 0:
            while n%i == 0:
                n //= i
            res += 1
    if n > 1 : res +=1
    if res >= 3: return True
    return False

if __name__ == '__main__':
    a, b = map(int, input().split())
    ok = True
    for i in range(a, b + 1):
        if check(i):
            ok = False
            print(i, end=' ')
    if ok:
        print(-1)