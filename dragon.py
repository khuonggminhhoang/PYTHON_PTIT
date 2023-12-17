if __name__ == '__main__':
    n, s = map(int, input().split())
    flag = True
    arr = []
    for i in range(n):
        a = list(map(int, input().split()))
        arr.append(a)
    arr.sort(key = lambda x : x[0])
    flag = True
    for x in arr:
        if s <= x[0]:
            flag = False
            break
        s += x[1]
    print('YES' if flag else 'NO')
    