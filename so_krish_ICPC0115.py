def isKrish(s):
    arr = list(s)
    sum = 0
    for x in arr:
        sum += fac[int(x)]
    return sum == int(s)

if __name__ == '__main__':
    fac = [0] * 10
    fac[0] = 1
    for i in range(1, 10):
        fac[i] = fac[i-1] * i
    t = int(input())
    while t != 0:
        n = input()
        print('Yes' if isKrish(n) else 'No')
        t-=1