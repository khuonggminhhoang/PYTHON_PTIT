if __name__ == '__main__':
    n = int(input())
    for test in range(n):
        s1 = list(input())
        s2 = list(input())
        s1.sort()
        s2.sort()
        print('Test ' + str(test + 1) + ': ', end='')
        if s1 == s2:
            print('YES')
        else:
            print('NO')