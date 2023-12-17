from math import *

fibo = [0] * (10**6 + 1)

def fibonacci():
    fibo[0], fibo[1] = 0, 1
    for i in range(2, 10**6 + 1):
        fibo[i] = fibo[i-1] + fibo[i-2]
        fibo[i]  %= (10**9 + 7)

if __name__ == '__main__':
    fibonacci()
    t = int(input())
    while t != 0:
        n = int(input())
        print(fibo[n])
        t -= 1
