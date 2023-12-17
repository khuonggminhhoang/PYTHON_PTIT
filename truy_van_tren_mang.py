if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    
    for _ in range(int(input())):
        n, x = map(int, input().split())
        if n == 1:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        elif n == 2:
            if x in d:
                d[x] -= 1
                if d[x] == 0:
                    d.pop(x)
        else:
            print('YES' if x in d else 'NO')