from math import *

prime = [True] * (10**6 + 1)
def sieve():
    prime[0] = prime[1] = False
    for i in range(2, isqrt(10**6 + 1) + 1):
        if prime[i] :
            for j in range(i*i, 10 ** 6 + 1, i):
                prime[j] = False


if __name__ == '__main__':
    sieve()
    for i in range(1000000):
        if prime[i]:
            print(i, end=' ')
