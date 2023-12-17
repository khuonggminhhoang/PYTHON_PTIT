def toNum(s):
    num = 0
    for x in s:
        num = num * 10 + int(x)
    return num

def replace(a, p, q):
    for i in range(len(a)):
            if a[i] == str(p):
                a[i] = str(q)
    return a

if  __name__ == '__main__':
    t = int(input())
    while t:
        p, q  = map(int, input().split())
        x = list(map(str, input().split()))
        if len(x) == 2:
            a, b = x
            a = list(a)
            b = list(b)
        else:
            a = list(x[0])
            b = list(input())

        replace(a, q, p)
        replace(b, q, p)
        tmp1 = toNum(a) + toNum(b)
        replace(a, p, q)
        replace(b, p, q)
        tmp2 = toNum(a) + toNum(b)
        print(min(tmp1, tmp2), max(tmp1, tmp2))
        t-=1