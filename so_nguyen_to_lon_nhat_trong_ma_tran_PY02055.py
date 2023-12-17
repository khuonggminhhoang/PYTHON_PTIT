from math import *

def is_prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    
    prime_max = 0
    for i in range(n):
        for j in range(m):
            if is_prime(a[i][j]) and a[i][j] > prime_max :
                prime_max = a[i][j]

    pos = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == prime_max:
                pos.append([i, j])

    if prime_max != 0:
        print(prime_max)
        for i, j in pos:
            print(f'Vi tri [{i}][{j}]')
    else:
        print('NOT FOUND')