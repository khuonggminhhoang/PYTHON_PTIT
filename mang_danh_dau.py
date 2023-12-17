from math import *

if __name__ == '__main__':
    a = [4, 2, 1, 2, 3, 1, 4, 2]
    cnt = [0] * 10000001
    for x in a:
        cnt[x] += 1
    
    l = min(a)
    r = max(a)
    for i in range(l, r + 1):
        print(i, cnt[i])