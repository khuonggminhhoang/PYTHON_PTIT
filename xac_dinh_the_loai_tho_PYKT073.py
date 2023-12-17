if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        s = input().split()
        a.append(len(s))
    
    lb = 0
    i = 0
    res = []
    while i < n:
        if a[i] == 6:
            if lb == 0:
                res.append(1)
                lb = 1
            i += 2
        else:
            lb = 0
            res.append(2)
            i += 4
    
    print(len(res))
    for x in res:
        print(x)
            