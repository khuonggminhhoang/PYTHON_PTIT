if __name__ == '__main__':
    t = int(input())
    while t:
        dct = {}
        n = int(input())
        maxx = -1
        for _ in range(n):
            x = int(input())
            if x in dct:
                dct[x] += 1
            else:
                dct[x] = 1
            maxx = max(maxx, dct[x])
        
        lst = list(dct.keys())
        lst.sort()
        for x in lst:
            if dct[x] == maxx:
                print(x)
                break

        t -= 1