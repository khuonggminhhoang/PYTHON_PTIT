if __name__ == '__main__':
    file = open('VANBAN.in', 'rt')
    data = file.read().split()
    dct = {}
    tmp = -1
    for x in data:
        if x == x[::-1]:
            tmp = max(tmp, len(x))
            if dct.get(x):
                dct[x] += 1
            else:
                dct[x] = 1
    for x in dct:
        if len(x) == tmp:
            print(x, dct[x])