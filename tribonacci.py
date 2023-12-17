from math import *

tribo = [0] * (10**6 + 1)
def tribonacci():
    tribo[0] = tribo[1] =0
    tribo[2] = 1
    for i in range(3, 10**6 + 1):
        tribo[i] = tribo[i-1] + tribo[i-2] + tribo[i-3]
        tribo[i] %= (10**9 + 7)

if __name__ =='__main__':
    tribonacci()
    t = int(input())
    while t != 0:
        n = int(input())
        print(tribo[n])
        t -= 1