if __name__ == '__main__':
    t = int(input())
    while t != 0:
        n = input()
        a = list(n)
        if a[0] == a[len(a) - 1]:
            flag = True
        else:
            flag = False
        print('YES' if flag else 'NO')
        t -= 1