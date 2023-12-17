import math

def isPrime(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i == 0:
            return False
    return n>1

def lastDigitMax(n):
    last = n%10
    while n!= 0:
        if last  < n%10:
            return False
        n//=10
    return True


if __name__ == '__main__':
    cnt = 0
    n = int(input())
    for i in range(2, n+1):
        if lastDigitMax(i) and isPrime(i):
            print(i, end=' ')
            cnt+=1
    print()
    print(cnt)