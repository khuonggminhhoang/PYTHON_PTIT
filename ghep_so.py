from functools import cmp_to_key

def cmp(a,b):
    ab = a + b
    ba = b + a
    if ab > ba:
        return -1
    else:
        return 1

if __name__ == '__main__':
    s = input()
    tmp = ''
    for x in s:
        if x.isalpha():
            tmp += ' '
        else:
            tmp += x
    arr = list(map(int, tmp.split()))
    mp = map(str, arr)
    for x in sorted(mp, key= cmp_to_key(cmp)):
        print(x, end='')