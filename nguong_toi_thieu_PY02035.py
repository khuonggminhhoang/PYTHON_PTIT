if __name__ == '__main__':
    s = input()
    if len(s) % 2 == 1:
        s = s[:-1]
    i = 0
    lst = []
    while i < len(s):
        lst += [int(s[i:i+2])]
        i += 2
    dct = {}
    for x in lst:
        if(dct.get(x)):
            dct[x] += 1
        else:
            dct[x] = 1
    
    n = int(input())
    lst = list(dct.keys())
    lst.sort()
    flag = True
    for x in lst:
        if dct[x] >= n:
            print(x, dct[x])
            flag = False
    if flag: print('NOT FOUND')