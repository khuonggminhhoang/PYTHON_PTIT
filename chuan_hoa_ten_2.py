if __name__ == '__main__':
    a = input().split()
    s1 = ''
    for i in range(len(a) - 1):
        s1 += a[i].capitalize() + ' '
    line1 = s1[0: len(s1) - 1] + ', ' + a[-1].upper() 
    print(line1)

    s2 = a[-1].upper() + ', ' + s1[0: len(s1) - 1]
    print(s2)