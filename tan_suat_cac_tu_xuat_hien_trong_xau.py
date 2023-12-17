if __name__ == '__main__':
    a = input().split()
    dct = dict()
    for x in a:
        if x in dct:
            dct[x] += 1
        else:
            dct[x] = 1

    for x in sorted(dct):
        print(x, dct[x])
    print()
    
    for key, value in dct.items():
        print(key, value)