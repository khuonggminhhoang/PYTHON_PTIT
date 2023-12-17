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
        dct[x] = 0
    st = list(dct.keys())
    print(*st)