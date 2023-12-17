import re

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = ''
    for _ in range(n):
        s += input() + ' '

    s = s.lower()

    arr = re.split('\W+', s)
    dct = {}
    
    for x in arr:
        if x != '':
            if dct.get(x):
                dct[x] += 1
            else:
                dct[x] = 1

    lst = [[o1, o2] for o1, o2 in dct.items()]
    lst.sort(key= lambda x : (-x[1], x[0]))

    for x in lst:
        if x[-1] >= k:
            print(*x)