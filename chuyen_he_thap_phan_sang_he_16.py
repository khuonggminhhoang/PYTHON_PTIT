def convertHex(n):
    if n == 0: return
    convertHex(n//16)
    tmp = n%16
    if tmp < 10:
        print(tmp, end= '')
    elif tmp == 10:
        print('A', end='')
    elif tmp == 11:
        print('B', end='')
    elif tmp == 12:
        print('C', end='')
    elif tmp == 13:
        print('D', end='')
    elif tmp == 14:
        print('E',end='')
    elif tmp == 15:
        print('F', end='')

if __name__ == '__main__':
    n = int(input())
    if n == 0:
        print(0)
    convertHex(n)


