def Try(index, total, n, tmparr, lst):
    if total == n:
        lst.append(tmparr)
    elif total < n:
        for i in range(index, 0, -1):
            Try(i, total + i, n, tmparr + ' ' + str(i), lst)
        
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        lst = []
        Try(n, 0, n, '', lst)
        print(len(lst))
        for s in lst:
            s = s.strip().split()
            print('(', end='')
            print(*s, end='')
            print(')', end=' ')
        print()
        
        t -= 1