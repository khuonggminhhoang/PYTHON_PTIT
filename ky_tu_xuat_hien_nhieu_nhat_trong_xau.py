if __name__ == '__main__':
    s = input()
    dct = dict()
    for x in s:
        if x in dct:
            dct[x] += 1
        else:
            dct[x] = 1
    mi = min(dct.values())
    ma = max(dct.values())
    
    for x in sorted(dct):
        if mi == dct[x]:
            ans1 = x
        if ma == dct[x]:
            ans2 = x
    
    print( ans2, ma)
    print(ans1, mi)
