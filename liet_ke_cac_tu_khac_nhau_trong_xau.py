if __name__ == '__main__':
    s = input()
    dct = dict()
    for x in s.split():
        dct[x] = 1
    for x in sorted(dct):
        print(x, end=' ')
    print()

    for x in dct:
        print(x, end=' ')

