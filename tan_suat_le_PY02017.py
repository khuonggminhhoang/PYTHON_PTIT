if __name__ == '__main__':
    t = int(input())
    while t :
        n = int(input())
        a = list(map(int, input().split()))
        dct = {}
        for x in a:
            if x in dct.keys():
                dct[x] += 1
            else:
                dct[x] = 1

        for x in dct:
            if dct[x] % 2 == 1:
                print(x)
                break

        t -= 1