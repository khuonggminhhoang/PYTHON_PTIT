if __name__ == '__main__':
    s = input()
    dct = dict()
    for x in s:
        if x in dct.keys():
            dct[x] += 1
        else : dct[x] = 1
    
    for x in sorted(dct):
        print(x, dct[x])
    print()

    for x, y in dct.items():
        print(x, y)