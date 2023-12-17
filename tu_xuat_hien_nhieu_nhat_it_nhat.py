if __name__ == '__main__':
    a = input().split()
    dct = dict()
    for x in a:
        if x in dct:
            dct[x] += 1
        else:
            dct[x] = 1
    
    mi = min(dct.values())
    ma = max(dct.values())

    for x in dct:
        if(dct[x] == ma):
            key_ma = x
        if(dct[x] == mi):
            key_mi = x
    
    print(key_ma, ma)
    print(key_mi, mi)