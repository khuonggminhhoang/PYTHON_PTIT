def check(n):
    while n :
        r = n%10
        if r != 0 and r != 6 and r != 8:
            return 0
        n //= 10
    return 1

if __name__ == '__main__':
    n = int(input())
    print(check(n))