def perfectNumber(n):
    while n != 0:
        tmp = n%10
        if tmp != 4 and tmp !=7:
            return False
        n //= 10
    return True

if __name__ == '__main__':
    t = int(input())
    while t !=0:
        n = int(input())
        print('YES' if perfectNumber(n) else 'NO')
        t -= 1

