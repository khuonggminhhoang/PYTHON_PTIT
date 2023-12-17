import re

if __name__ == '__main__':
    n = int(input())
    s = ''
    for _ in range(n):
        s += input() + ' '
    s = s.lower()
    dct = {}
    arr = re.split('\W+', s)
    for x in arr:
        if x != '':
            if dct.get(x):
                dct[x] += 1
            else:
                dct[x] = 1
    
    lst = [[x, y] for x, y in dct.items()]
    lst.sort(key= lambda x: (-x[1], x[0]))
    for x in lst:
        print(*x)
