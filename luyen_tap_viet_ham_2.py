import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

def function1(n):
    if n == 0 : return 1
    cntEven = 0
    while n!=0 :
        if (n%10) %2 == 0:
            cntEven += 1
        n //= 10
    if cntEven % 2 == 1 : return 1
    return 0

def function2(n):
    if n == 0 : return 1
    cntEven = 0
    cntOdd = 0
    while n != 0 :
        if n%2 ==0: cntEven += 1
        else: cntOdd +=1
        n //= 10
    if cntEven > cntOdd : return 1
    return 0

def function3(n):
    last = n%10
    while n >= 10:
        n //= 10
    if last == n : return 1
    return 0

def function4(n):
    sum = 0
    while n != 0:
        sum += n%10
        n //= 10
    if sum%10 == 8: return 1
    return 0

def function5(n):
    sum = 0
    while n:
        sum += n%10
        n //= 10
    if isPrime(sum) : return 1
    return 0

def function6(n):
    while n >= 10 :
        if abs(n%10 - (n//10)%10) != 1: return 0
        n //= 10
    return 1

def function7(n):
    maxCur = -1
    while n >= 10:
        maxCur = max(maxCur, n%10)
        n //= 10
    if n > maxCur: return 1
    return 0

def fibo(x):
    if x ==0 or x == 1: return True
    fn1 = 1; fn2 = 0
    for i in range(2,93):
        fn = fn1 + fn2
        if x == fn : return True
        fn2 = fn1; 
        fn1 = fn
    return False

def function8(n):
    sum = 0
    while n != 0 :
        sum += n%10
        n //= 10
    if fibo(sum) : return 1
    return 0

def checkReverseNum(m):
    tmp = m
    tmpNum = 0
    while tmp != 0:
        tmpNum = tmpNum * 10 + tmp % 10
        tmp //= 10
    if m == tmpNum: return True
    return False

def function9(n):
    sum = 0
    while n :
        sum += n%10
        n //= 10
    if checkReverseNum(sum) : return 1
    return 0

def function10(n):
    while n != 0 :
        if n%10 != 0 and n%10 != 6 and n%10 != 8:
            return 0
        n //= 10
    return 1

if __name__ == '__main__':
    t = int(input())
    while t :
        n = int(input())
        print(function1(n))
        print(function2(n))
        print(function3(n))
        print(function4(n))
        print(function5(n))
        print(function6(n))
        print(function7(n))
        print(function8(n))
        print(function9(n))
        print(function10(n))
        t-=1