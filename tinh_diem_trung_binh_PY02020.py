if __name__ == '__main__':
    n = int(input())
    a = list(map(float, input().split()))
    x = min(a)
    y = max(a)
    while x in a:
        a.remove(x)
    while y in a:
        a.remove(y)
    ans = sum(a)/(len(a))
    print('%.2f' %ans)