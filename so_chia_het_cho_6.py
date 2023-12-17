if __name__ == '__main__':
    s = input()
    a = [int(x) for x in s]
    if sum(a) % 3 == 0 and a[-1] % 2 == 0:
        print('YES')
    else:
        print('NO')