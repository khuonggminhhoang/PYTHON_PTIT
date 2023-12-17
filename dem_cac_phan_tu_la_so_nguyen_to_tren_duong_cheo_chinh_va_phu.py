from math import *

def isPrime(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    cnt = 0
    st = set()
    for i in range(n):
        if isPrime(a[i][i]):
            cnt += 1
            st.add(a[i][i])
        if i != n - i - 1 and isPrime(a[i][n - i - 1]):
            cnt += 1
            st.add(a[i][n - i - 1])
    print(cnt)
    print(len(st))
