from math import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * n
    min_, max_ = int(1e9), -int(1e9)
    for i in range(n):
        a[i] = list(map(int, input().split()))
        min_ = min(min_, min(a[i]))
        max_ = max(max_, max(a[i]))

    tmp = max_ - min_
    pos = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == tmp:
                pos.append([i, j])

    if len(pos) != 0:
        print(tmp)
        for i, j in pos:
            print(f'Vi tri [{i}][{j}]')
    else:
        print('NOT FOUND')