import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

def funct1(n):
    return (1 if isPrime(n) else 0)

def funct2(n):
    sum = 0
    while n!=0:
        sum += n%10
        n//=10
    return sum

def funct3(n):
    sum = 0
    while n!= 0:
        if((n%10) %2 == 0):
            sum += n%10
        n//=10
    return sum

def funct4(n):
    sum = 0
    while n != 0 :
        r = n%10
        if r == 2 or r == 3 or r == 5 or r == 7:
            sum += r
        n //= 10
    return sum

def funct5(n):
    ans = 0
    while n!= 0 :
        ans = ans * 10 + n%10
        n //= 10
    return ans

def funct6(n):
    ans = 0
    for i in range(2, math.isqrt(n) +1):
        if n % i == 0:
            ans+=1 
            while(n % i == 0):
                n//=i
    if n > 1: ans += 1
    return ans

def funct7(n):
    ans = 0
    for i in range(2, math.isqrt(n) +1):
        if n % i == 0:
            ans = i
            while n%i == 0:
                n //= i
    if n > 1 : ans = n
    return ans

def funct8(n):
    while n!=0:
        if n%10 == 6:
            return 1
        n//=10
    return 0

def funct9(n):
    sum = 0
    while n:
        sum += n%10
        n //= 10
    if sum % 8 ==0 : return 1
    return 0

def funct10(n):
    sum = 0
    while n!= 0:
        tmp = 1
        r = n % 10
        for i in range(1, r + 1):
            tmp *= i
        sum += tmp
        n //= 10
    return sum

def funct11(n):
    tmp = n%10
    while n!=0:
        if n%10 != tmp:
            return 0
        n //= 10
    return 1

def funct12(n):
    last = n%10
    while n!=0:
        if n%10 > last:
            return 0
        n //= 10
    return 1

def funct13(n):
    cnt = 0
    tmp = n
    while n!= 0:
        n//=10
        cnt+=1
    ans = 0
    while tmp!=0 :
        ans += (tmp%10)**cnt
        tmp //= 10
    return ans

if __name__ == '__main__':
    n = int(input())
    print(funct1(n))
    print(funct2(n))
    print(funct3(n))
    print(funct4(n))
    print(funct5(n))
    print(funct6(n))
    print(funct7(n))
    print(funct8(n))
    print(funct9(n))
    print(funct10(n))
    print(funct11(n))
    print(funct12(n))
    print(funct13(n))