def solve(lst1, lst2, lst3):
    dct1 = {}
    dct2 = {}
    dct3 = {}
    for x in lst1:
        if dct1.get(x): dct1[x] += 1
        else: dct1[x] = 1

    for x in lst2:
        if dct2.get(x): dct2[x] += 1
        else: dct2[x] = 1

    for x in lst3:
        if dct3.get(x): dct3[x] += 1
        else: dct3[x] = 1

    flag = True
    for x in dct1:
        if x in dct2 and x in dct3:
            m = min(dct1[x], dct2[x], dct3[x])
            for i in range(m):
                print(x, end=' ')
                flag = False
    if flag: print('NO', end='')
    print()

if __name__ == '__main__':
    t = int(input())
    while t :
        n, m, k = map(int, input().split())
        lst1 = list(map(int, input().split()))
        lst2 = list(map(int, input().split()))
        lst3 = list(map(int, input().split()))  
        solve(lst1, lst2, lst3)

        t -= 1