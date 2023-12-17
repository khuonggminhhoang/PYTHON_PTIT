from math import *

def is_palin(n):
    n = str(n)
    if len(n) == 1 : return False
    return n == n[::-1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    
    palin_max = 0
    for i in range(n):
        for j in range(m):
            if is_palin(a[i][j]) and a[i][j] > palin_max :
                palin_max = a[i][j]

    pos = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == palin_max:
                pos.append([i, j])

    if palin_max != 0:
        print(palin_max)
        for i, j in pos:
            print(f'Vi tri [{i}][{j}]')
    else:
        print('NOT FOUND')