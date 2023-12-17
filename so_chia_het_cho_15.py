if __name__ == '__main__':
    s = input()
    a = [int(x) for x in s]
    if sum(a) % 3 == 0 and (a[-1] == 0 or a[-1] == 5):
        print('YES') 
    else:
        print('NO')