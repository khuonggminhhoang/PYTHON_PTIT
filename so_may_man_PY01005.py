def luckyNumber(n):
    cnt4 = 0
    cnt7 = 0
    while n != 0:
        tmp = n%10
        if tmp == 4:
            cnt4 += 1
        if tmp == 7:
            cnt7 += 1
        n //= 10
    if cnt4 + cnt7 == 7 or cnt4 + cnt7 == 4:
        return True
    return False

if __name__ == '__main__':
    n = int(input())
    print('YES' if luckyNumber(n) else 'NO')