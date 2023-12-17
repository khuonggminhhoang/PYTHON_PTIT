from sys import stdin

def increase(s):
    for i in range(len(s) - 1):
        if int(s[i]) > int(s[i + 1]):
            return False
    return True

if __name__ == '__main__':
    a= []
    for line in stdin:
        a += list(line.split())

    dct = dict()
    for x in a:
        if increase(x):
            if x in dct:
                dct[x] += 1
            else: dct[x] = 1
    ans = list(dct.items())
    ans.sort(key= lambda x : (-x[1], int(x[0])))
    for x, y in ans:
        print(x,y)


