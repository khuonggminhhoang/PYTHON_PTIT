from math import *

if __name__ == '__main__':
    l, r = map(int,input().split())
    for i in range(l, r-1):
        for j in range(i + 1, r):
            if gcd(i,j) == 1:
                for k in range(j + 1, r + 1):
                    if gcd(j,k) == 1 and gcd(i,k) == 1:
                        print("({:d}, {:d}, {:d})".format(i,j,k))